import os
from pathlib import Path
from typing import List, Tuple


def discover_files(target_dir: str) -> List[Tuple[str, str]]:

    supported_extensions = {".py", ".md", ".rst", ".txt", ".mdx"}
    discoverd: List = []

    base_path = Path(target_dir)
    if not base_path.exists():
        raise FileNotFoundError(f"Directory not found: {target_dir}")

    for root, _, files in os.walk(target_dir):
        for file in files:
            ext = Path(file).suffix.lower()
            if ext in supported_extensions:
                full_path = os.path.join(root, file)
                norm_path = os.path.normpath(full_path).replace("\\", "/")
                try:
                    with open(full_path, "r") as f:
                        content = f.read()
                    if content.strip():
                        discoverd.append((norm_path, content))
                except Exception:
                    print("Warning: Failed to read {full_path}: {e}")
    return discoverd


def chunk_document(file: str, content: str, max_size: int = 2000
                   ) -> List:
    ext = Path(file).suffix.lower()
    if ext == ".py":
        return chunk_python_file(file, content, max_size)
    elif ext in {}:
        return chunk_markdown(file, content, max_size)
    else:
        pass

def chunk_python_file(file: str, content: str, max_size: int):
    chunks = []
