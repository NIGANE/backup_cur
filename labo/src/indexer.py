from src.chunker import MinimalSource, Error, Chunker
from typing import List, Tuple, Dict
import math
from pathlib import Path
import os
import pickle
from pydantic import BaseModel



class BM25Index(BaseModel):
    term_freqs: List[Dict[str, int]]
    doc_lens: List[int]
    avg_dl: float
    idf: Dict[str, float]
    chunks: List[MinimalSource]


class Indexer():
    def __init__(self, dest: str):
        self.tokens: List[List[str]] = []
        self.chunks: List[Tuple[MinimalSource, str]] = []
        self.res_file_name: str = "bm25_index.pkl"
        try:
            os.makedirs(dest, exist_ok=True)
        except Exception as e:
            raise Error(f"IndexerError: {e}")
        self.dest: Path = Path(dest) / self.res_file_name
        self.t_freq: List[Dict[str, int]] = []
        self.doc_freq: Dict[str, int] = {}
        self.len: Tuple[List[int], float] = ([], 0.0)
        self.idfre: Dict[str, float] = {}
        self.last_resolved: List[MinimalSource] = []

    def tokenize_chunks(self, src: str) -> Path:
        self.chunks = Chunker.load(src)
        if (not self.chunks):
            return Path('')
        self.tokens = [self.split(src[1]) for src in self.chunks]
        self.t_freq: List[Dict[str, int]] = self.term_frequency(self.tokens)
        self.doc_freq: Dict[str, int] = self.doc_frequency(self.tokens)
        self.len: Tuple[List[int], float] = self.lenth(self.tokens)
        self.idfre: Dict[str, float] = self.idf(self.doc_freq, len(self.tokens))
        self.export:BM25Index = BM25Index(
            term_freqs=self.t_freq,
            doc_lens=self.len[0],
            avg_dl=self.len[1],
            idf=self.idfre,
            chunks=[ch[0] for ch in self.chunks]
        )
        return self.save()

    def split(self, src: str) -> List[str]:
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

    def search(self, query: List[str], ind: BM25Index,
               k1: float = 1.5, b: float = 0.75) -> List[Tuple[float, int]]:

        scores = [0.0] * len(ind.term_freqs)
        for id, tf_dict in enumerate(ind.term_freqs):
            dl = ind.doc_lens[id]
            d_score = 0.0
            for token in query:
                if token not in ind.idf:
                    continue

                tf = tf_dict.get(token, 0)
                if tf == 0:
                    continue

                idf_val = ind.idf[token]
                numerator = tf * (k1 + 1.0)
                denominator = tf + k1 * (1.0 - b + b * (dl / ind.avg_dl))

                d_score += idf_val * (numerator / denominator)
            scores[id] = d_score
        res: List[Tuple[float, int]] = [(scores[i], i) for i in range(len(scores)) if scores[i] > 0.0]
        res.sort(key=lambda x: x[0], reverse=True)
        return res



    def save(self) -> Path:
        try:
            with open(self.dest, "wb") as f:
                pickle.dump(self.export, f)
        except Exception as e:
            raise Error(f"ChunkerError: {e}")
        else:
            print(f"index successfully saved -> {self.dest}")
            return self.dest

    def load(self, dest: str) -> BM25Index:
        if (not Path(dest).exists()):
            raise FileNotFoundError(
                f"FileNotFound: chunked file not found on '{dest}"
                )
        try:
            with open(dest, "rb") as f:
                self.export = pickle.load(f)
                return self.export
        except Exception as e:
            raise Error(e)

    def fetch_query_chunks(self, sc: List[Tuple[float, int]], k: int = 5):
        ret = []
        self.last_resolved = []
        if len(sc) <= k:
            ret = sc
        else:
            ret = [sc[i] for i in range(0, k)]
        for _, id in ret:
            source = self.export.chunks[id]
            self.last_resolved.append(source)
            print(f"{source.file_path} [{source.first_character_index}:{source.last_character_index}]")