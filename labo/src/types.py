from typing import TypedDict, List, Dict, Tuple
from src.models import MinimalSource
from pydantic import BaseModel, ConfigDict
import numpy as np


class RagQuestion(TypedDict):
    question_id: str | None
    question: str


class BM25Index(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    mtime_index_file: float
    term_freqs: List[Dict[str, int]] | None
    doc_lens: List[int] | None
    avg_dl: float | None
    idf: Dict[str, float] | None
    chunks: List[MinimalSource] | None
    embedding: np.ndarray | None


class SearchResults(TypedDict):
    question_id: str
    question: str
    sources: List[MinimalSource]


class ChunkResuls(BaseModel):
    chunks: List[Tuple[MinimalSource, str]]
    ut_files: Dict[str, float]
