from src.models import (StudentSearchResults, MinimalSource,
                        MinimalAnswer, StudentSearchResultsAndAnswer)
from typing import Dict, List, Optional, Any, Tuple
from src.error import Error, DataValidation
from src.indexer import BM25Index
from pydantic_core import ErrorDetails
from pydantic import ValidationError
from src.types import RagQuestion
from src.error import UsageError
from src.chunker import Chunker
from src.agent import Agent
from pathlib import Path
from tqdm import tqdm
import json
from src.lexical_index import LexicalIndexer
from src.hybrid_index import HybridIndexer
# import numpy as np


class Controller:
    def __init__(self):
        pass

    @staticmethod
    def validate_paths(*paths: Tuple[str, str]) -> None:
        for p in paths:
            if (p[1] is True or not p[1]):
                raise UsageError(
                    f"missing 1 required positional argument '{p[0]}'")

    @staticmethod
    def validate_numeric(*numbers: Tuple[str, int | str | None, int]) -> None:
        for n in numbers:
            if (isinstance(n[1], str) and not n[1].isnumeric()):
                raise UsageError(
                    f"arg '{n[0]}' is not an integer")
            if (isinstance(n[1], int) and n[1] <= n[2]):
                raise UsageError(
                    f"'{n[0]}' must be valid integer with "
                    f"the range -> '{n[0]} >= {n[2]}'")
            if (isinstance(n[1], bool)):
                raise UsageError(
                    f"missing 1 optional argument value '--{n[0]}'?")

    @staticmethod
    def fetch_json(path: Path) -> Any:
        if (not path.exists()):
            raise FileNotFoundError(f"file not found '{path}'")
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise Error(e)

    @staticmethod
    def index(path: Path, hybrid: str = '', max_chunk_size: int = 2000
              ) -> None:
        Controller.validate_numeric(
            ("max_chunk_size", max_chunk_size, 1)
        )
        if (isinstance(hybrid, str) and len(hybrid) > 0):
            raise UsageError(f"unknown argument '{hybrid}'")

        chunker = Chunker(str(path / 'raw'), str(path / 'process'))
        cnk_path = chunker.discover_files().chunk()
        if (hybrid is True):
            indexer: HybridIndexer = HybridIndexer(str(path / 'process'))
        else:
            indexer: LexicalIndexer = LexicalIndexer(str(path / 'process'))
        dest: Path = indexer.tokenize_chunks(str(cnk_path))
        if (not dest):
            return Controller.index(path, hybrid, max_chunk_size)
        print(f"Ingestion complete! Indices saved under {dest.parent}")

    @staticmethod
    def search(query: str = '', path: Path = Path(''), k: int = 5,
               hybrid: str = '') -> None:
        Controller.validate_paths(
            ("query", query)
        )
        Controller.validate_numeric(
            ("k", k, 1)
        )
        if (isinstance(hybrid, str) and len(hybrid) > 0):
            raise UsageError(f"unknown argument '{hybrid}'")

        ps_path: Path = path / 'process'
        if (hybrid is True):
            ind: HybridIndexer = HybridIndexer(str(ps_path))
        else:
            ind: LexicalIndexer = LexicalIndexer(str(ps_path))
        loads: Optional[BM25Index] = ind.load(ps_path)
        if (not loads):
            Controller.index(path, hybrid)
            return Controller.search(query, path, k, hybrid)
        sources: List[MinimalSource] = []
        bm25_scores: List[Tuple[float, int]] = ind.search(query, loads)
        if (hybrid is True):
            if (loads.embedding is None):
                raise UsageError("embedding did found on loads.\n"
                                 "run index with --hybrid then try again")
            sources = ind.hybrid_resolve(loads.embedding, bm25_scores, query)
        else:
            sources = ind.fetch_query_chunks(bm25_scores, k)
        for source in sources:
            print(f"{source.file_path} [{source.first_character_index}:",
                  f"{source.last_character_index}]", sep="")

    @staticmethod
    def search_dataset(dataset_path: str = '', k: int = 5,
                       save_directory: str = '', path: Path = Path(''),
                       hybrid: str = '') -> None:
        Controller.validate_paths(
            ("dataset_path", dataset_path),
            ("save_directory", save_directory)
        )
        Controller.validate_numeric(
            ('k', k, 1)
        )
        if (isinstance(hybrid, str) and len(hybrid) > 0):
            raise UsageError(f"unknown argument '{hybrid}'")

        src = Path(dataset_path)
        data: Dict[str, List[RagQuestion]] = Controller.fetch_json(src)
        if (not data):
            raise UsageError(f"the feeded file is empty '{src}'")
        if (not data.get('rag_questions')):
            raise UsageError(
                'given file doesnt contain rag_questions'
                f"{src}")
        if (hybrid is True):
            indexer: HybridIndexer = HybridIndexer(save_directory)
        else:
            indexer: LexicalIndexer = LexicalIndexer(save_directory)
        loads: Optional[BM25Index] = indexer.load(path / 'process')
        if (not loads):
            Controller.index(path, hybrid)
            return Controller.search_dataset(
                dataset_path, k, save_directory, path, hybrid)
        dest: Path = indexer.search_multy(data, loads, k)
        print(f"Saved student_search_results to {dest}")

    @staticmethod
    def answer(query: str = '', k: int = 5, hybrid: str = '',
               path: Path = Path('')) -> None:
        if (query == ''):
            raise UsageError("missing 1 required positional argument 'qeury'")
        Controller.validate_numeric(
            ("k", k, 1)
        )
        if (isinstance(hybrid, str) and len(hybrid) > 0):
            raise UsageError(f"unknown argument '{hybrid}'")

        ps_path: Path = path / 'process'
        if (hybrid is True):
            ind: HybridIndexer = HybridIndexer(str(ps_path))
        else:
            ind: LexicalIndexer = LexicalIndexer(str(ps_path))
        loads: Optional[BM25Index] = ind.load(ps_path)
        if (not loads):
            Controller.index(path, hybrid)
            return Controller.search(query, path, k, hybrid)

        sources: List[MinimalSource] = []
        bm25: List[Tuple[float, int]] = ind.search(query, loads)
        if (hybrid is True):
            if (loads.embedding is None):
                raise UsageError("embedding did found on loads.\n"
                                 "run index with --hybrid then try again")
            sources = ind.hybrid_resolve(loads.embedding, bm25, query,
                                         loads.chunks)[:k]
        else:
            sources = ind.fetch_query_chunks(bm25, k)

        agent: Agent = Agent()
        res: Dict[str, str] = agent.inference(sources, query)
        print("Answer: ", res['generated_text'])

    @staticmethod
    def answer_dataset(student_search_results_path: str = '',
                       save_directory: str = '',
                       path: Path = Path('')):

        Controller.validate_paths(
            ("student_search_results_path", student_search_results_path),
            ("save_directory", save_directory)
        )

        src: Path = Path(student_search_results_path)
        d_search: Any = Controller.fetch_json(src)
        try:
            obj: StudentSearchResults = StudentSearchResults.model_validate(
                d_search)
        except ValidationError as e:
            err: ErrorDetails = e.errors()[0]
            raise DataValidation(f"{err['type']} {err['loc'][0]}, {err['msg']}"
                                 + "on data source" +
                                 f"{src}")
        print(f"loaded {len(obj.search_results)} questions ...")
        data: List[MinimalAnswer] = []
        agent: Agent = Agent()
        with tqdm(obj.search_results,
                  desc="Answering", unit=" Qestion") as update:
            for ele in update:
                res = agent.inference(ele.retrieved_sources, ele.question)
                data.append(
                    MinimalAnswer(
                        question_id=ele.question_id,
                        question=ele.question,
                        retrieved_sources=ele.retrieved_sources,
                        answer=res['generated_text']
                    )
                )
        res = StudentSearchResultsAndAnswer(
            search_results=data,
            k=obj.k
        )
        dest: Path = agent.save(res, Path(save_directory))
        print(f"Saved student_search_results_and_answer to {dest}")

    @staticmethod
    def evaluate(student_search_results_path: str = '',
                 dataset_path: str = ''):
        Controller.validate_paths(
            ("student_search_results_path", student_search_results_path),
            ("dataset_path", dataset_path)
        )
        student_sr = Controller.fetch_json(Path(student_search_results_path))
        source_of_truth = Controller.fetch_json(Path(dataset_path))
        if (not student_sr):
            raise ValueError("Student resutls file found empty!")
        if (not source_of_truth):
            raise ValueError("Dataset file is empty")
        try:
            obj: StudentSearchResults = StudentSearchResults.model_validate(
                student_sr)
        except ValidationError as e:
            err: ErrorDetails = e.errors()[0]
            raise DataValidation(f"{err['type']} {err['loc'][0]}, {err['msg']}"
                                 + " on data source -> " +
                                 f"{student_search_results_path}")
        pass

