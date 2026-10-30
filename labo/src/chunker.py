from src.models import MinimalSource
from pydantic import ValidationError
from typing import List, Tuple, Any, Dict
from src.types import ChunkResuls
from src.error import Error
from pathlib import Path
from tqdm import tqdm
import pickle
import ast
import os
import re


class Chunker:
    exported_format: str = "chunks.pkl"

    def __init__(self, src: str, dest: str = 'data/process',
                 max_size: int = 2000) -> None:
        self.chunks: List[Tuple[MinimalSource, str]] = []
        self.src: str = src
        self.discovered_files: List[Tuple[str, str]] = []
        self.max_size: int = max_size
        try:
            os.makedirs(dest, exist_ok=True)
        except SystemError as e:
            raise Error(e)
        self.dest: Path = Path(dest)
        self.chunk_file_path: Path = self.discover_files()

    @staticmethod
    def get_file_mtime(file_path: str) -> float:
        return os.path.getmtime(file_path)

    @staticmethod
    def changed_file(old_mtime: float, file_path: str
                     ) -> bool:
        return (old_mtime != Chunker.get_file_mtime(file_path))

    def discover_files(self) -> Path:

        supported_extensions = {".py", ".md", ".rst", ".txt", ".mdx"}
        discoverd: List[Tuple[str, str]] = []

        expanded_dir = os.path.expanduser(self.src)
        base_path: Path = Path(expanded_dir)
        if not base_path.exists():
            raise FileNotFoundError(f"Directory not found '{self.src}'")

        for root, _, files in os.walk(self.src):
            for file in files:
                ext = Path(file).suffix.lower()
                if ext in supported_extensions:
                    full_path = os.path.join(root, file)
                    norm_path = os.path.normpath(full_path).replace("\\", "/")
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        if content.strip():
                            discoverd.append((norm_path, content))
                    except Exception as e:
                        print(f"Warning: Failed to read {full_path}: {e}")
        if (not discoverd):
            raise Error(f"Emtpy given repo to parse on '{self.src}'")
        ut_files: Dict[str, float] = {}
        if (self.dest / self.exported_format).exists():
            try:
                old_file: Any = self.load(
                    str(self.dest / self.exported_format))
                old_data: ChunkResuls = ChunkResuls.model_validate(old_file)
            except ValidationError:
                self.discovered_files = discoverd
            else:
                self.discovered_files = self.filter_files(old_file, discoverd)
                for f in discoverd:
                    if f not in self.discovered_files:
                        ut_files[f[0]] = old_data.ut_files[f[0]]
        else:
            self.discovered_files = discoverd
        self.chunk()
        for f in self.discovered_files:
            ut_files[f[0]] = self.get_file_mtime(f[0])

        data: ChunkResuls = ChunkResuls(
            chunks=self.chunks,
            ut_files=ut_files
        )
        return self.save(data)

    def chunk(self) -> None:
        if (len(self.discovered_files) == 0):
            return
        with tqdm(
                self.discovered_files, desc="Chunking",
                unit=" file") as group:
            for f in group:
                self.chunks.extend(self.chunk_document(f[0], f[1]))

    def blind_chunker(self, target_file: str, source: str, curr_offset: int,
                      max_size: int) -> List[Tuple[MinimalSource, str]]:

        chunks: List[Tuple[MinimalSource, str]] = []
        lines: List[str] = source.splitlines(keepends=True)

        curr_chunk: str = ""
        curr_start: int = curr_offset
        running_offset: int = curr_offset

        for line in lines:
            if len(curr_chunk) + len(line) > max_size and curr_chunk:
                ob = MinimalSource(
                    file_path=target_file,
                    first_character_index=curr_start,
                    last_character_index=curr_start + len(curr_chunk),
                )
                chunks.append((ob, curr_chunk))
                curr_start = running_offset
                curr_chunk = ""

            if len(line) > max_size:
                for i in range(0, len(line), max_size):
                    sub_line = line[i:i + max_size]
                    ob = MinimalSource(
                        file_path=target_file,
                        first_character_index=running_offset + i,
                        last_character_index=running_offset + i + len(sub_line)
                    )
                    chunks.append((ob, sub_line))
                running_offset += len(line)
                curr_start = running_offset
            else:
                curr_chunk += line
                running_offset += len(line)

        if curr_chunk:
            ob = MinimalSource(
                file_path=target_file,
                first_character_index=curr_start,
                last_character_index=curr_start + len(curr_chunk),
            )
            chunks.append((ob, curr_chunk))

        return chunks

    def chunk_document(self, file: str, content: str, max_size: int = 2000
                       ) -> List[Tuple[MinimalSource, str]]:
        ext: str = Path(file).suffix.lower()
        chunks = []
        if ext == ".py":
            chunks = self.python_chunker(file, content, max_size)
        elif ext in {".md", ".rst", ".txt", ".mdx"}:
            chunks = self.regular_chunker(file, content, max_size)
        else:
            chunks = self.blind_chunker(file, content, 0, max_size)
        self.chunks = [*chunks, *self.chunks]
        return chunks

    def regular_chunker(
        self, target_file: str, content: str, max_size: int
    ) -> List[Tuple[MinimalSource, str]]:

        chunks: List[Tuple[MinimalSource, str]] = []
        header_pattern = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
        matches = list(header_pattern.finditer(content))

        if not matches:
            return self.blind_chunker(target_file, content, 0, max_size)

        indexes = [m.start() for m in matches] + [len(content)]

        if indexes[0] > 0 and content[0:indexes[0]].strip():
            chunks.extend(
                self.blind_chunker(
                    target_file, content[0:indexes[0]], 0,
                    max_size))

        for i in range(len(matches)):
            start_idx = indexes[i]
            end_idx = indexes[i + 1]
            txt = content[start_idx:end_idx]

            if len(txt) <= max_size:
                source = MinimalSource(
                    file_path=target_file,
                    first_character_index=start_idx,
                    last_character_index=end_idx,
                )
                chunks.append((source, txt))
            else:
                chunks.extend(
                    self.blind_chunker(
                        target_file, txt, start_idx, max_size
                    ))

        return chunks

    def python_chunker(self, target_file: str, content: str, max_size: int
                       ) -> List[Tuple[MinimalSource, str]]:
        chunks: List[Tuple[MinimalSource, str]] = []
        last_end: int = 0

        try:
            tree = ast.parse(content)
        except Exception:
            return self.blind_chunker(target_file, content, 0, max_size)

        nodes: List[ast.FunctionDef | ast.ClassDef | ast.AsyncFunctionDef] = [
                node for node in tree.body
                if isinstance(
                    node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)
                    )
                ]
        if (not nodes):
            return self.blind_chunker(target_file, content, 0, max_size)
        lines: List[str] = content.splitlines(True)

        for node in nodes:
            start: int = sum(len(lines[i]) for i in range(node.lineno - 1))
            end: int = sum(len(lines[i]) for i in range(node.end_lineno))

            if (last_end != start):
                hole = content[last_end:start]
                if hole.strip():
                    chunks.extend(self.blind_chunker(target_file, hole,
                                                     last_end, max_size))

            chunk: str = content[start:end]
            if (len(chunk) > max_size):
                chunks.extend(self.blind_chunker(target_file, chunk,
                                                 start, max_size))
            else:
                source: MinimalSource = MinimalSource(
                        file_path=target_file,
                        first_character_index=start,
                        last_character_index=end
                    )
                chunks.append((source, chunk))
            last_end = end
        if (last_end < len(content)):
            reminder: str = content[last_end:]
            if reminder.strip():
                chunks.extend(
                    self.blind_chunker(
                        target_file, reminder, last_end, max_size
                        )
                    )
        return (chunks)

    def save(self, data: ChunkResuls) -> Path:
        try:
            with open(self.dest / self.exported_format, "wb") as f:
                pickle.dump(data, f)
        except Exception as e:
            raise Error(f"ChunkerError: {e}")
        else:
            return self.dest / self.exported_format

    @staticmethod
    def load(dest: str) -> ChunkResuls:
        if (not Path(dest).exists()):
            raise FileNotFoundError(
                f"chunke file not found on '{Path(dest).parent}"
                )
        try:
            with open(dest, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            raise Error(e)

    def __repr__(self):
        print("-- chunks : ", "---" * 10)
        for ch in self.chunks:
            print(f"chunk: {ch[0].file_path} ",
                  f"({ch[0].first_character_index}",
                  f"-{ch[0].last_character_index}) ",
                  f"{len(ch[1])} bytes",
                  sep="")
        return ''

    def filter_files(self, old_load: ChunkResuls, new: List[Tuple[str, str]]):
        res: List[Tuple[str, str]] = []
        for f in new:
            if (f[0] in old_load.ut_files.keys()
                    and self.changed_file(old_load.ut_files[f[0]], f[0])):
                res.append(f)
            else:
                old: Tuple[MinimalSource, str] | None = self.get_source(
                    old_load.chunks, f[0])
                if (old is not None):
                    self.chunks.append(old)
        res.extend([f for f in new if f[0] not in old_load.ut_files.keys()])

        return res

    def get_source(self, chunks: List[Tuple[MinimalSource, str]],
                   path: str) -> Tuple[MinimalSource, str] | None:
        for el in chunks:
            if el[0].file_path == path:
                return el
        return None

    @staticmethod
    def get_chunk(obj: MinimalSource):
        path: Path = Path(obj.file_path)
        st: int = obj.first_character_index
        end: int = obj.last_character_index
        if (not path.exists()):
            raise (FileNotFoundError(f"target file not found '{path}'"))
        try:
            with open(path, 'r') as f:
                f.seek(st)
                return f.read(end - st)
        except Exception as e:
            raise Error(e)
