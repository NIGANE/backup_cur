from collections import defaultdict
from pathlib import Path
from tqdm import tqdm
import numpy as np
from src.indexer import Indexer
from src.chunker import Chunker
from typing import List, Dict, Tuple
from src.types import BM25Index, RagQuestion, SearchResults
from sentence_transformers import SentenceTransformer
from src.models import (MinimalSource,
                        StudentSearchResults, MinimalSearchResults)
import uuid
from src.error import UsageError


class HybridIndexer(Indexer):
    def __init__(self, dest: str = '', llm: str = "all-MiniLM-L6-v2"):
        super().__init__(dest)
        self.model: SentenceTransformer = SentenceTransformer(llm)

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
        embedding: np.ndarray | None = self.vectorize(data)
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
            embedding=embedding
        )
        return self.save()

    def search(self, query: str, ind: BM25Index, k1: float = 1.5,
               b: float = 0.75) -> List[Tuple[float, int]]:

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
        if (ind.embedding is None):
            raise UsageError("embedding did found on loads.\n"
                             "run index with --hybrid then try again")

        qts = [
            dict(
                question=qt.get("question"),
                question_id=qt.get("question_id")
            )
            for qt in data['rag_questions']
            ]
        with tqdm(qts, desc="Searching", unit=" Question") as group:
            for qt in group:
                if (qt['question'] is None
                        or qt["question"] in [ele["question"] for ele in res]):
                    continue
                bm25 = self.search(qt['question'].lower(), ind)
                res.append({
                    "question_id": qt.get("question_id") or str(uuid.uuid4()),
                    "question": qt["question"],
                    "sources": self.hybrid_resolve(
                        ind.embedding, bm25, qt["question"], ind.chunks)[:k]
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

    def hybrid_resolve(self, embedding, bm25, query: str,
                       chunks: List[MinimalSource]):
        query_vectore: np.ndarray = self.vectorize(query)
        vector_scores: np.ndarray = self.cosine_similarity(
            embedding, query_vectore)
        self.last_resolved = self.rrf(vector_scores, bm25, chunks)
        return self.last_resolved

    def vectorize(self, data: List[str] | str) -> np.ndarray:
        return self.model.encode(data, convert_to_numpy=True)

    def cosine_similarity(self, chunk_embeddings: np.ndarray,
                          query_vector: np.ndarray) -> np.ndarray:
        dot_products = np.dot(chunk_embeddings, query_vector)
        query_norm = np.linalg.norm(query_vector)
        chunk_norms = np.linalg.norm(chunk_embeddings, axis=1)

        scores = dot_products / (query_norm * chunk_norms + 1e-9)
        return scores

    def rrf(self, vector_scores: np.ndarray,
            bm25_scores: List[Tuple[float, int]],
            chunks: List[MinimalSource], k: int = 5, k_rrf: int = 60
            ) -> List[MinimalSource]:

        # 1. Rank and slice top 20 candidates from vector scores
        vector_ranked_indices = np.argsort(vector_scores)[::-1][:20]
        vector_ranked = [(float(vector_scores[idx]), int(idx))
                         for idx in vector_ranked_indices]

        # 2. Slice top 20 candidates from bm25 scores
        bm25_ranked = bm25_scores[:20]

        rrf_scores = defaultdict(float)

        # 3. Accumulate RRF scores from BM25
        for rank, (score, chunk_idx) in enumerate(bm25_ranked, start=1):
            rrf_scores[chunk_idx] += 1.0 / (k_rrf + rank)

        # 4. Accumulate RRF scores from Vector search
        for rank, (score, chunk_idx) in enumerate(vector_ranked, start=1):
            rrf_scores[chunk_idx] += 1.0 / (k_rrf + rank)

        # 5. Sort fused results descending by RRF score
        sorted_hybrid = sorted(rrf_scores.items(), key=lambda x: x[1],
                               reverse=True)

        # 6. Map back to top K MinimalSource objects
        top_sources = []
        for chunk_idx, _ in sorted_hybrid[:k]:
            source_meta = chunks[chunk_idx]
            top_sources.append(source_meta)

        return top_sources
