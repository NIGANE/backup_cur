from src.models import StudentSearchResults, MinimalSearchResults
from src.types import BM25Index, RagQuestion, SearchResults
from src.chunker import MinimalSource, Error, Chunker
from typing import List, Tuple, Dict, Optional
from sentence_transformers import SentenceTransformer
from collections import Counter, defaultdict
from pathlib import Path
from tqdm import tqdm
import numpy as np
import pickle
import math
import json
import uuid
import os


class Indexer():
    def __init__(self, dest: str = '', hybrid_search: bool = False):
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
        self.hybrid_search: bool = hybrid_search
        if (self.dest.suffix):
            file: str = self.dest.name
            self.dest = self.dest.parent
            self.dataset_file = self.dataset_answer_file = file

    def tokenize_chunks(self, src: str) -> Path:
        self.chunks = Chunker.load(src)
        data: List[str] = []
        if (not self.chunks):
            return Path('')
        with tqdm(
                self.chunks, desc="Tokenizing",
                unit=" chunks", total=len(self.chunks) + 5
                ) as group:
            for e in group:
                self.tokens.append(self.split(e[1]))
                data.append(e[1])
        embedgin: np.ndarray | None = (self.vectorize(data)
                                       if self.hybrid_search else None)
        self.t_freq: List[Dict[str, int]] = self.term_frequency(self.tokens)
        self.doc_freq: Dict[str, int] = self.doc_frequency(self.tokens)
        self.len: Tuple[List[int], float] = self.lenth(self.tokens)
        self.idfre: Dict[str, float] = self.idf(
            self.doc_freq, len(self.tokens)
            )

        self.export: BM25Index = BM25Index(
            term_freqs=self.t_freq,
            doc_lens=self.len[0],
            avg_dl=self.len[1],
            idf=self.idfre,
            chunks=[ch[0] for ch in self.chunks],
            embedding=embedgin
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
        return dict(Counter(src))          # O(L) instead of O(L²)

    def term_frequency(self, src: List[List[str]]) -> List[Dict[str, int]]:
        return [dict(Counter(doc)) for doc in src]

    def doc_frequency(self, src: List[List[str]]) -> Dict[str, int]:
        df: Counter = Counter()
        for doc in src:
            df.update(set(doc))            # each word counted once per doc
        return dict(df)                    # O(total tokens)

    def lenth(self, src: List[List[str]]) -> Tuple[List[int], float]:
        lens = [len(doc) for doc in src]
        return lens, (sum(lens) / len(lens) if lens else 0.0)

    def idf(self, fq: Dict[str, int], size: int) -> Dict[str, float]:
        idf: Dict[str, float] = {}
        for w, f in fq.items():
            val = math.log(1.0 + (size - f + 0.5) / (f + 0.5))
            idf[w] = max(0.0, val)
        return idf

    def search(self, query: str, ind: BM25Index,
               k1: float = 1.5, b: float = 0.75) -> List[Tuple[float, int]]:
        query_tokens: List[str] = self.split(query)
        scores = [0.0] * len(ind.term_freqs)
        for id, tf_dict in enumerate(ind.term_freqs):
            dl = ind.doc_lens[id]
            d_score = 0.0
            for token in query_tokens:
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
        res: List[Tuple[float, int]] = [
            (scores[i], i) for i in range(len(scores)) if scores[i] > 0.0
            ]
        res.sort(key=lambda x: x[0], reverse=True)
        return res

    def search_multy(self, data: Dict[str, List[RagQuestion]],
                     ind: BM25Index, k: int = 5):

        res: List[SearchResults] = []

        qts = [
            dict(
                question=qt.get("question"),
                question_id=qt.get("question_id")
            )
            for qt in data['rag_questions']
            ]
        for qt in qts:
            if (qt['question'] is None
                    or qt["question"] in [ele["question"] for ele in res]):
                continue
            scores = self.search(qt['question'].lower(), ind)
            res.append({
                "question_id": qt.get("question_id") or str(uuid.uuid4()),
                "question": qt["question"],
                "sources": self.fetch_query_chunks(scores, k)
            })

        self.dataset_search = StudentSearchResults(
            search_results=[
                MinimalSearchResults(
                    question_id=ele['question_id'],
                    question=ele['question'],
                    retrieved_sources=ele['sources']
                ) for ele in res
            ],
            k=k
        )
        return self.save_dataset()

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

    def vectorize(self, data: List[str] | str, llm: str = "all-MiniLM-L6-v2"
                  ) -> np.ndarray:
        model = SentenceTransformer(llm)
        return model.encode(data, convert_to_numpy=True)

    def 

    def cosine_similarity(self, chunk_embeddings: np.ndarray,
                          query_vector: np.ndarray):
        dot_products = np.dot(chunk_embeddings, query_vector)

        query_norm = np.linalg.norm(query_vector)
        chunk_norms = np.linalg.norm(chunk_embeddings, axis=1)

        scores = dot_products / (query_norm * chunk_norms + 1e-9)
        return scores

    def rrf(self, vector_scores, bm25_scores,
            chunks: List[MinimalSource],
            k: int = 5, k_rrf: int = 60) -> List[MinimalSource]:

        vector_ranked_indices = np.argsort(vector_scores)[::-1][:20]
        vector_ranked = [(float(vector_scores[idx]), int(idx))
                         for idx in vector_ranked_indices]

        rrf_scores = defaultdict(float)

        for rank, (score, chunk_idx) in enumerate(bm25_scores, start=1):
            rrf_scores[chunk_idx] += 1.0 / (k_rrf + rank)

        for rank, (score, chunk_idx) in enumerate(vector_ranked, start=1):
            rrf_scores[chunk_idx] += 1.0 / (k_rrf + rank)

        sorted_hybrid = sorted(rrf_scores.items(), key=lambda x: x[1],
                               reverse=True)

        top_sources = []
        for chunk_idx, _ in sorted_hybrid[:k]:
            source_meta = chunks[chunk_idx]
            top_sources.append(source_meta)

        return top_sources

