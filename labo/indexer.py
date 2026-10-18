from chunker import MinimalSource, Error
from typing import List, Tuple, Any, Dict
from chunker import Chunker
import math
from pathlib import Path
import os
import pickle


class Indexer():
    def __init__(self, dest: str):
        self.tokens: List[List[str]] = []
        self.chunks: List[Tuple[MinimalSource, str]] = []
        self.res_file_name: str = "bm25_index.pkl"
        try:
            os.makedirs(dest, exist_ok=True)
        except Exception as e:
            raise Error(e)
        self.dest: Path = Path(dest) / self.res_file_name
        self.term_fr: List[Dict[str, int]] = []
        

    def tokenize_chunks(self, src: str) -> List[List[str]]:
        self.chunks = Chunker.load(src)
        if (not self.chunks):
            return []
        self.tokens = [self.split(src[1]) for src in self.chunks]
        return self.tokens

    def split(self, src: str):
        res: List[str] = []
        buffer: List[str] = []
        src = src.strip()
        num = False
        for i, e in enumerate(src):
            if (e.isalnum()):
                if e.isnumeric():
                    if buffer and not num and i > 0 and not src[i - 1].isalnum():
                        res.append("".join(buffer))
                        buffer = []
                    buffer.append(str(e))
                    num = True
                    continue
                if (num):
                    num = False
                    if (buffer):
                        res.append("".join(buffer))
                    buffer = []
                if e.isupper():
                    if buffer and i > 0 and src[i - 1].islower():
                        res.append("".join(buffer))
                        buffer = []
                    buffer.append(e.lower())
                else:
                    buffer.append(e.lower())
                if (i == len(src) - 1):
                    if (buffer):
                        res.append("".join(buffer))
            else:
                if (buffer):
                    res.append("".join(buffer))
                buffer = []
        return res

    def term_frequency(self, src: List[List[str]]) -> List[Dict[str, int]]:
        res: List[Dict[str, int]] = []
        for ch in src:
            res.append(self.fr(ch))
        return res

    def fr(self, src: List[str]) -> Dict[str, int]:
        res: Dict[str, int] = {}
        for e in src:
            cn: int = 0
            if (e in res.keys()):
                continue
            for bf in src:
                if bf == e:
                    cn += 1
            res[e] = cn
        return res

    def lenth(self, src: List[List[str]]) -> Tuple[List[int], float]:
        return (
            [len(doc) for doc in src],
            sum([len(doc) for doc in src]) / len(src)
            )

    def doc_frequency(self, src: List[List[str]]) -> Dict[str, int]:
        res: Dict[str, int] = {}
        for doc in src:
            for w in doc:
                if w in res.keys():
                    continue
                res[w] = sum([1 for e in src if w in e])
        return res

    def idf(self, fq: Dict[str, int], size: int) -> Dict[str, float]:
        idf: Dict[str, float] = {}
        for w, f in fq.items():
            val = math.log(1.0 + (size - f + 0.5) / (f + 0.5))
            idf[w] = max(0.0, val)
        return idf

    # def bm25_index

    def save(self) -> Path:
        try:
            with open(self.dest, "wb") as f:
                pickle.dump(self.chunks, f)
        except Exception as e:
            raise Error(f"ChunkerError: {e}")
        else:
            print(f"index successfully saved -> {self.dest}")
            return self.dest

    @staticmethod
    def load(dest) -> List[Tuple[MinimalSource, str]]:
        if (not Path(dest).exists()):
            raise FileNotFoundError(
                f"FileNotFound: chunked file not found on '{dest}"
                )
        try:
            with open(dest, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            raise Error(e)