from typing import TypedDict, List, Dict
from src.models import MinimalSource
from pydantic import BaseModel


class RagQuestion(TypedDict):
    question_id: str | None
    question: str


class BM25Index(BaseModel):
    term_freqs: List[Dict[str, int]]
    doc_lens: List[int]
    avg_dl: float
    idf: Dict[str, float]
    chunks: List[MinimalSource]


class SearchResults(TypedDict):
    question_id: str
    question: str
    sources: List[MinimalSource]
