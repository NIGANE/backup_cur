from src.models import StudentSearchResults, MinimalSearchResults
from src.types import BM25Index, RagQuestion, SearchResults, ChunkResuls
from src.chunker import MinimalSource, Error, Chunker
from typing import List, Tuple, Dict, Optional, Any
from src.indexer import Indexer
from pathlib import Path
from tqdm import tqdm
from pydantic import ValidationError
from src.error import DataValidation
import pickle
import json
import uuid
import os


class LexicalIndexer(Indexer):

    def tokenize_chunks(self) -> Path:
        if (self.index_file_founded()):
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
                unit=" chunks"
                ) as group:
            for e in group:
                self.tokens.append(self.split(e[1]))
                data.append(e[1])
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
            embedding=None
        )
        return self.save()

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
        with tqdm(qts, desc="Searching", unit=" Question") as group:
            for qt in group:
                if (qt['question'] is None
                        or qt["question"] in [ele["question"] for ele in res]):
                    continue
                scores = self.search(qt['question'].lower())
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
        ret: List[Tuple[float, int]] = []
        self.last_resolved = []
        if len(sc) <= k:
            ret = sc
        else:
            ret = [sc[i] for i in range(0, k)]
        for _, id in ret:
            source = self.export.chunks[id]
            self.last_resolved.append(source)
        return self.last_resolved
