from src.models import (StudentSearchResults, MinimalSource,
                        MinimalAnswer, StudentSearchResultsAndAnswer)
from typing import Dict, List, Optional, Any, Tuple
from src.error import Error, DataValidation
from src.indexer import Indexer, BM25Index
from pydantic_core import ErrorDetails
from pydantic import ValidationError
from src.types import RagQuestion
from src.error import UsageError
from src.chunker import Chunker
from src.agent import Agent
from pathlib import Path
from tqdm import tqdm
import json


class Controller:
    def __init__(self):
        pass

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
    def index(path: Path, max_chunk_size: int = 2000) -> None:
        if (isinstance(max_chunk_size, str)
                and not max_chunk_size.isnumeric()):
            raise UsageError(f"arg '{max_chunk_size}' is not an integer")

        chunker = Chunker(str(path / 'raw'), str(path / 'process'))
        cnk_path = chunker.discover_files().chunk()
        indexer = Indexer(str(path / 'process'))
        dest: Path = indexer.tokenize_chunks(str(cnk_path))
        if (not dest):
            return Controller.index(path, max_chunk_size)
        print(f"Ingestion complete! Indices saved under {dest.parent}")

    @staticmethod
    def search(query: str = '', path: Path = Path(''), k: int = 5) -> None:
        if (query == ''):
            raise UsageError("missing 1 required positional argument 'qeury'")
        if (isinstance(k, str) and not k.isnumeric()):
            raise UsageError(f"arg '{k}' is not an integer")
        if (isinstance(k, bool)):
            raise UsageError("missing 1 optional argument value '--k'?")
        ps_path: Path = path / 'process'

        ind: Indexer = Indexer(str(ps_path))
        loads: Optional[BM25Index] = ind.load(ps_path)
        if (not loads):
            Controller.index(path)
            return Controller.search(query, path, k)

        scores: List[Tuple[float, int]] = ind.search(query, loads)
        sources: List[MinimalSource] = ind.fetch_query_chunks(scores, k)
        for source in sources:
            print(f"{source.file_path} [{source.first_character_index}:",
                  f"{source.last_character_index}]", sep="")

    @staticmethod
    def search_dataset(dataset_path: str = '', k: int = 5,
                       save_directory: str = '', path: Path = Path('')
                       ) -> None:
        if (dataset_path is True or not dataset_path):
            raise UsageError(
                "missing 1 required positional argument 'dataset_path'")
        if (save_directory is True or not save_directory):
            raise UsageError(
                "missing 1 required positional argument 'save_directory'")
        if (isinstance(k, str) and not k.isnumeric()):
            raise UsageError(f"arg '{k}' is not an integer")
        if (isinstance(k, bool)):
            raise UsageError("missing 1 optional argument value '--k'?")
        src = Path(dataset_path)
        data: Dict[str, List[RagQuestion]] = Controller.fetch_json(src)
        if (not data):
            raise UsageError(f"the feeded file is empty '{src}'")
        if (not data.get('rag_questions')):
            raise UsageError(
                'given file doesnt contain rag_questions'
                f"{src}")
        indexer: Indexer = Indexer(save_directory)
        loads: Optional[BM25Index] = indexer.load(path / 'process')
        if (not loads):
            Controller.index(path)
            return Controller.search_dataset(
                dataset_path, k, save_directory, path)

        dest: Path = indexer.search_multy(data, loads, k)
        print(f"Saved student_search_results to {dest}")

    @staticmethod
    def answer(query: str = '', k: int = 5, path: Path = Path('')):
        if (query == ''):
            raise UsageError("missing 1 required positional argument 'qeury'")
        if (isinstance(k, str) and not k.isnumeric()):
            raise UsageError(f"arg '{k}' is not an integer")
        ps_path: Path = path / 'process'
        if (isinstance(k, bool)):
            raise UsageError("missing 1 optional argument value '--k'?")
        ind: Indexer = Indexer(str(ps_path))
        loads: Optional[BM25Index] = ind.load(ps_path)
        if (not loads):
            Controller.index(path)
            return Controller.search(query, path, k)

        scores = ind.search(query, loads)
        ind.fetch_query_chunks(scores, k)

        agent: Agent = Agent()
        res: Dict[str, str] = agent.inference(ind.last_resolved, query)
        print("Answer: ", res['generated_text'])

    @staticmethod
    def answer_dataset(student_search_results_path: str = '',
                       save_directory: str = '',
                       path: Path = Path('')):

        if (not student_search_results_path
                or student_search_results_path is True):
            raise UsageError(
                "missing 1 required positional argument "
                "'--student_search_results_path'"
                )
        if (not save_directory or save_directory is True):
            raise UsageError(
                "missing 1 required positional argument '--save_directory'"
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
