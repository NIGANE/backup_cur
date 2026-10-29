from src.models import StudentSearchResults
from src.types import BM25Index
from src.chunker import MinimalSource, Error
from typing import List, Tuple, Dict, Optional
from collections import Counter
from pathlib import Path
import pickle
import math
import json
import os


class Indexer():
    def __init__(self, dest: str = ''):
        self.tokens: List[List[str]] = []
        self.chunks: List[Tuple[MinimalSource, str]] = []
        self.res_file_name: str = "bm25_index.pkl"
        self.dataset_file: str = 'dataset_docs_public.json'
        self.dataset_answer_file: str = "answer_dataset_docs_public.json"
        self.dest: Path = Path(dest)
        self.t_freq: List[Dict[str, int]] = []
        self.doc_freq: Dict[str, int] = {}
        self.len: Tuple[List[int], float] = ([], 0.0)
        self.idfre: Dict[str, float] = {}
        self.last_resolved: List[MinimalSource] = []
        self.dataset_search: StudentSearchResults
        if (self.dest.suffix):
            file: str = self.dest.name
            self.dest = self.dest.parent
            self.dataset_file = self.dataset_answer_file = file

    def split(self, src: str) -> List[str]:
        res: List[str] = []
        buffer: List[str] = []
        src = src.strip()
        num = False
        for i, e in enumerate(src):
            if (e.isalnum()):
                if e.isnumeric():
                    if (buffer and not num and i > 0
                            and not src[i - 1].isalnum()):
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

    # def term_frequency(self, src: List[List[str]]) -> List[Dict[str, int]]:
    #     res: List[Dict[str, int]] = []
    #     for ch in src:
    #         res.append(self.fr(ch))
    #     return res

    # def fr(self, src: List[str]) -> Dict[str, int]:
    #     res: Dict[str, int] = {}
    #     for e in src:
    #         cn: int = 0
    #         if (e in res.keys()):
    #             continue
    #         for bf in src:
    #             if bf == e:
    #                 cn += 1
    #         res[e] = cn
    #     return res

    # def lenth(self, src: List[List[str]]) -> Tuple[List[int], float]:
    #     return (
    #         [len(doc) for doc in src],
    #         sum([len(doc) for doc in src]) / len(src)
    #         )

    # def doc_frequency(self, src: List[List[str]]) -> Dict[str, int]:
    #     res: Dict[str, int] = {}
    #     for doc in src:
    #         for w in doc:
    #             if w in res.keys():
    #                 continue
    #             res[w] = sum([1 for e in src if w in e])
    #     return res

    def fr(self, src: List[str]) -> Dict[str, int]:
        return dict(Counter(src))

    def term_frequency(self, src: List[List[str]]) -> List[Dict[str, int]]:
        return [dict(Counter(doc)) for doc in src]

    def doc_frequency(self, src: List[List[str]]) -> Dict[str, int]:
        df: Counter = Counter()
        for doc in src:
            df.update(set(doc))
        return dict(df)

    def lenth(self, src: List[List[str]]) -> Tuple[List[int], float]:
        lens = [len(doc) for doc in src]
        return lens, (sum(lens) / len(lens) if lens else 0.0)

    def idf(self, fq: Dict[str, int], size: int) -> Dict[str, float]:
        idf: Dict[str, float] = {}
        for w, f in fq.items():
            val = math.log(1.0 + (size - f + 0.5) / (f + 0.5))
            idf[w] = max(0.0, val)
        return idf

    def save(self) -> Path:
        try:
            os.makedirs(self.dest, exist_ok=True)
            with open(self.dest / self.res_file_name, "wb") as f:
                pickle.dump(self.export, f)
        except Exception as e:
            raise Error(f"{e}")
        else:
            return self.dest / self.res_file_name

    def save_dataset(self) -> Path:
        try:
            os.makedirs(self.dest, exist_ok=True)

            with open(self.dest / self.dataset_file, 'w') as f:
                json.dump(
                    self.dataset_search.model_dump(),
                    f,
                    indent=2
                    )
        except Exception as e:
            raise Error(e)
        else:
            return self.dest / self.dataset_file

    def load(self, dest: Path) -> Optional[BM25Index]:
        if (not (dest / self.res_file_name).exists()):
            return None

        try:
            with open(dest / self.res_file_name, "rb") as f:
                self.export = pickle.load(f)
                return self.export
        except Exception as e:
            raise Error(e)

    def fetch_query_chunks(self, sc: List[Tuple[float, int]], k: int = 5
                           ) -> List[MinimalSource]:
        ret = []
        self.last_resolved = []
        if len(sc) <= k:
            ret = sc
        else:
            ret = [sc[i] for i in range(0, k)]
        for _, id in ret:
            source = self.export.chunks[id]
            self.last_resolved.append(source)
        return self.last_resolved
