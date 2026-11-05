from pathlib import Path
from tqdm import tqdm
import numpy as np
from src.indexer import Indexer
from src.chunker import Chunker
from typing import List, Dict, Tuple, Any
from src.types import BM25Index, RagQuestion, SearchResults, ChunkResuls
from sentence_transformers import SentenceTransformer
from src.models import (MinimalSource,
                        StudentSearchResults, MinimalSearchResults)
import uuid
from src.error import DataValidation, UsageError
from pydantic import ValidationError


class VectorIndexer(Indexer):
    def __init__(self, dest: str = 'data/process',
                 llm: str = "all-MiniLM-L6-v2"):
        super().__init__(dest)
        self.model: SentenceTransformer = SentenceTransformer(llm)

    def tokenize_chunks(self) -> Path:
        if (self.index_file_founded(vector=True)):
            return self.dest / self.res_file_name

        try:
            loads: Any = Chunker.load(str(self.dest / Chunker.exported_format))
            obj: ChunkResuls = ChunkResuls.model_validate(loads)
            self.chunks = obj.chunks
        except ValidationError as e:
            raise DataValidation(e)

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
            mtime_index_file=Chunker.get_file_mtime(
                str(self.dest / Chunker.exported_format)),
            term_freqs=self.t_freq,
            doc_lens=self.len[0],
            avg_dl=self.len[1],
            idf=self.idfre,
            chunks=[ch[0] for ch in self.chunks],
            embedding=embedding
        )
        return self.save()

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
                res.append({
                    "question_id": qt.get("question_id") or str(uuid.uuid4()),
                    "question": qt["question"],
                    "sources": self.vector_search(
                        ind.embedding, qt["question"], ind.chunks, k)
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

    def vector_search(self, embedding, query: str,
                      chunks: List[MinimalSource], k: int = 5):
        query_vector: np.ndarray = self.vectorize(query)
        vector_scores: np.ndarray = self.cosine_similarity(
            embedding, query_vector)
        vector_scores = np.argsort(vector_scores)[::-1]
        self.last_resolved = [chunks[int(id)] for id in vector_scores][:k]
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
