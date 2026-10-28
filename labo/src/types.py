from typing import TypedDict, List, Dict
from src.models import MinimalSource
from pydantic import BaseModel, ConfigDict
import numpy as np


class RagQuestion(TypedDict):
    question_id: str | None
    question: str


class BM25Index(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    term_freqs: List[Dict[str, int]]
    doc_lens: List[int]
    avg_dl: float
    idf: Dict[str, float]
    chunks: List[MinimalSource]
    embedding: np.ndarray | None


class SearchResults(TypedDict):
    question_id: str
    question: str
    sources: List[MinimalSource]
