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
from src.vector_index import VectorIndexer
import sys
import os
from django.core.management import execute_from_command_line



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
            if (isinstance(n[1], int) and n[1] < n[2]):
                raise UsageError(
                    f"'{n[0]}' must be valid integer with "
                    f"the range  '{n[0]} >= {n[2]}'")
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
    def index(path: Path, hybrid: str = '', vector: str = '',
              max_chunk_size: int = 2000
              ) -> None:
        Controller.validate_numeric(
            ("max_chunk_size", max_chunk_size, 1)
        )
        if isinstance(vector, str) and len(vector) > 0:
            raise UsageError(f"unkonwn argument '{vector}'")
        if (isinstance(hybrid, str) and len(hybrid) > 0):
            raise UsageError(f"unknown argument '{hybrid}'")
        if hybrid is True and vector is True:
            raise UsageError("must use only one flag [--hybrid | --vector]")

        Chunker(str(path / 'raw'), max_size=max_chunk_size)
        if (hybrid is True):
            indexer: HybridIndexer = HybridIndexer()
        elif vector is True:
            indexer: VectorIndexer = VectorIndexer()
        else:
            indexer: LexicalIndexer = LexicalIndexer()
        dest: Path = indexer.tokenize_chunks()
        if (not dest):
            return Controller.index(path, hybrid, vector, max_chunk_size)
        print(f"Ingestion complete! Indices saved under {dest.parent}")

    @staticmethod
    def search(query: str = '', path: Path = Path(''), k: int = 5,
               hybrid: str = '', vector: str = '') -> None:
        Controller.validate_paths(
            ("query", query)
        )
        Controller.validate_numeric(
            ("k", k, 1)
        )
        if (isinstance(hybrid, str) and len(hybrid) > 0):
            raise UsageError(f"unknown argument '{hybrid}'")
        if (isinstance(vector, str) and len(vector) > 0):
            raise UsageError(f"unknown argument '{vector}'")
        if hybrid is True and vector is True:
            raise UsageError("must use only one flag [--hybrid | --vector]")

        ps_path: Path = path / 'process'
        if (hybrid is True):
            ind: HybridIndexer = HybridIndexer(str(ps_path))
        elif (vector is True):
            ind: VectorIndexer = VectorIndexer()
        else:
            ind: LexicalIndexer = LexicalIndexer(str(ps_path))
        loads: Optional[BM25Index] = ind.load(ps_path)

        if (not loads):
            Controller.index(path, hybrid, vector)
            return Controller.search(query, path, k, hybrid, vector)
        sources: List[MinimalSource] = []
        bm25_scores: List[Tuple[float, int]] | None = (
            ind.search(query) if not vector else None)
        if (hybrid is True or vector is True) and loads.embedding is None:
            raise UsageError("embeddings are not founded on index file.\n"
                             "run index with --vector then try again")
        if (hybrid is True):
            sources = ind.hybrid_resolve(
                loads.embedding, bm25_scores, query, loads.chunks, k)
        elif vector is True:
            sources = ind.vector_search(
                loads.embedding, query, loads.chunks, k)
        else:
            if bm25_scores:
                sources = ind.fetch_query_chunks(bm25_scores, k)
        for source in sources:
            print(f"{source.file_path} [{source.first_character_index}:",
                  f"{source.last_character_index}]", sep="")

    @staticmethod
    def search_dataset(dataset_path: str = '', k: int = 5,
                       save_directory: str = '', path: Path = Path(''),
                       hybrid: str = '', vector: str = '') -> None:
        Controller.validate_paths(
            ("dataset_path", dataset_path),
            ("save_directory", save_directory)
        )
        Controller.validate_numeric(
            ('k', k, 1)
        )
        if (isinstance(hybrid, str) and len(hybrid) > 0):
            raise UsageError(f"unknown argument '{hybrid}'")
        if (isinstance(vector, str) and len(vector) > 0):
            raise UsageError(f"unknown argument '{vector}'")

        src = Path(dataset_path)
        data: Dict[str, List[RagQuestion]] = Controller.fetch_json(src)
        if (not data):
            raise UsageError(f"the feeded file is empty '{src}'")
        if (not data.get('rag_questions')):
            raise UsageError(
                'given file doesnt contain rag_questions'
                f"{src}")
        if (hybrid is True and vector is True):
            raise UsageError("must use only one flag [--hybrid | --vector]")

        if (hybrid is True):
            indexer: HybridIndexer = HybridIndexer(save_directory)
        elif vector is True:
            indexer: VectorIndexer = VectorIndexer(save_directory)
        else:
            indexer: LexicalIndexer = LexicalIndexer(save_directory)

        loads: Optional[BM25Index] = indexer.load(path / 'process')
        if (not loads):
            Controller.index(path, hybrid, vector)
            return Controller.search_dataset(
                dataset_path, k, save_directory, path, hybrid, vector)
        if (hybrid is True or vector is True) and loads.embedding is None:
            raise UsageError("embeddings are not founded on index file.\n"
                             "run index with --vector then try again")

        dest: Path = indexer.search_multy(data, loads, k)
        print(f"Saved student_search_results to {dest}")

    @staticmethod
    def answer(query: str = '', k: int = 5, hybrid: str = '',
               path: Path = Path(''), vector: str = '') -> None:
        if (query == ''):
            raise UsageError("missing 1 required positional argument 'qeury'")
        Controller.validate_numeric(
            ("k", k, 1)
        )
        if (isinstance(hybrid, str) and len(hybrid) > 0):
            raise UsageError(f"unknown argument '{hybrid}'")
        if (isinstance(vector, str) and len(vector) > 0):
            raise UsageError(f"unknown argument '{vector}'")
        if (vector is True and hybrid is True):
            raise UsageError("must use only one flag [--hybrid | --vector]")

        ps_path: Path = path / 'process'
        if (hybrid is True):
            ind: HybridIndexer = HybridIndexer()
        elif (vector is True):
            ind: VectorIndexer = VectorIndexer()
        else:
            ind: LexicalIndexer = LexicalIndexer()
        loads: Optional[BM25Index] = ind.load(ps_path)
        if (not loads):
            Controller.index(path, hybrid, vector)
            return Controller.search(query, path, k, hybrid, vector)
        if (hybrid is True or vector is True) and loads.embedding is None:
            raise UsageError("embeddings are not founded on index file.\n"
                             "run index with --vector then try again")

        sources: List[MinimalSource] = []
        bm25: List[Tuple[float, int]] | None = (
            ind.search(query) if not vector else None)
        if (hybrid is True):
            sources = ind.hybrid_resolve(loads.embedding, bm25, query,
                                         loads.chunks, k)
        elif (vector is True):
            sources = ind.vector_search(
                loads.embedding, query, loads.chunks, k)
        else:
            if bm25:
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
                                 + " on data source" +
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
    
    @staticmethod
    def api(*args):
        src_dir = Path(__file__).resolve().parent
        if str(src_dir) not in sys.path:
            sys.path.insert(0, str(src_dir))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.core.settings')
        sys.argv = ["manage.py", "runserver", "localhost:8080"]
        execute_from_command_line(sys.argv)
        
