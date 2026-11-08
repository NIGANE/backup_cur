from rest_framework.decorators import api_view
from rest_framework.response import Response
from typing import Tuple, Optional, List, Dict, Any
from src.error import UsageError, DataValidation
from src.chunker import Chunker
from src.lexical_index import LexicalIndexer
from src.hybrid_index import HybridIndexer
from src.vector_index import VectorIndexer
from pathlib import Path
from src.types import BM25Index
from src.controller import Controller as ctr
from src.models import (MinimalSource, StudentSearchResults, MinimalAnswer,
                        StudentSearchResultsAndAnswer)
from pydantic import ValidationError
from pydantic_core import ErrorDetails
import os
from rest_framework import status
from src.agent import Agent
from tqdm import tqdm
from src.core.serializer import SearchSerializer

class Controller:
    @staticmethod
    def validate_record(record: Tuple[str, str]) -> str:
        if (record[1] is None or (isinstance(record[1], str) and record[1] == "")):
            raise UsageError(
                f"missing 1 required positional argument '{record[0]}'")
        return record[1]

    @staticmethod
    def validate_numeric(num: Tuple[str, str | None, int]) -> None | int:
        if num[1] is None:
            return None
        if (isinstance(num[1], str) and not num[1].isnumeric()):
            raise UsageError(
                f"arg '{num[0]}' is not a valid integer given ('{num[1]}')")
        
        if (int(num[1]) < num[2]):
            raise UsageError(
                f"'{num[0]}' must be valid integer with "
                f"the range  '{num[0]} >= {num[2]}'")
        return int(num[1])
    
    @staticmethod
    def validate_flags(flag: Tuple[str, str | None]) -> bool:
        if flag[1] is None or flag[1] == "False":
            return False
        if isinstance(flag[1], str) and (flag[1] != "True"):
            raise UsageError(f"incorected type for {flag[0]} allowed [True | False]")
        return bool(flag[1])
    
    @staticmethod
    def validate_dataset(data: Tuple[str, dict | None]) -> Dict[str, Any] | None:
        if not isinstance(data[1], dict):
            raise UsageError("dataset is not valid")
        if len(data[1]) < 1:
            raise UsageError("dataset is empty")
        return data[1]
        

    @staticmethod
    @api_view(['GET'])
    def index(req) -> Response:
        try:
            vector: bool | None = Controller.validate_flags(
                ('vector', req.data.get('vector'))
            )
            hybrid: bool | None = Controller.validate_flags(
                ('hybrid', req.data.get('hybrid'))
            )
            size: int = Controller.validate_numeric((
                    "max_chunk_size",
                    req.data.get('max_chunk_size'),
                    2000
                 )) or 2000

            if (vector is True and hybrid is True):
                raise UsageError("must use only one flag ['vector' | 'hybrid']")

            Chunker(max_size=size)
            if (hybrid is True):
                indexer: HybridIndexer = HybridIndexer()
            elif vector is True:
                indexer: VectorIndexer = VectorIndexer()
            else:
                indexer: LexicalIndexer = LexicalIndexer()
            dest: Path = indexer.tokenize_chunks()
            if (not dest):
                raise SystemError("Internal Error")
            mess: str = f"Ingestion complete! Indices saved under {dest.parent}"
            print(mess)
            return Response({
                "message": f"Ingestion complete! Indices saved under {dest.parent}"
            },status=status.HTTP_200_OK)
        except (BaseException, UsageError) as e:
            return Response({
                "error": e.__str__()
            },
            status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    @api_view(['POST'])
    def search(req) -> Response:
        try:
            vector: bool | None = Controller.validate_flags(
                ('vector', req.data.get('vector'))
            )
            hybrid: bool | None = Controller.validate_flags(
                ('hybrid', req.data.get('hybrid'))
            )
            query: str = Controller.validate_record(
                ("query", req.data.get('query'))
            )
            k: int = Controller.validate_numeric(
                ('k', req.data.get('k'), 1)
            ) or 5
            if (vector is True and hybrid is True):
                raise UsageError("must use only one flag ['vector' | 'hybrid']")
            if (hybrid is True):
                ind: HybridIndexer = HybridIndexer()
            elif (vector is True):
                ind: VectorIndexer = VectorIndexer()
            else:
                ind: LexicalIndexer = LexicalIndexer()

            loads: Optional[BM25Index] = ind.load(ind.dest)
            if (not loads):
                print("no loads founded\ngenerating new index files")
                ctr.index(ind.dest.parent, hybrid, vector)
                return Controller.search(req._request)
            sources: List[MinimalSource] = []
            bm25_scores: List[Tuple[float, int]] | None = (
                ind.search(query) if not vector else None)
            if (hybrid is True or vector is True) and loads.embedding is None:
                raise UsageError("embeddings are not founded on index file")

            if (hybrid is True):
                sources = ind.hybrid_resolve(
                    loads.embedding, bm25_scores, query, loads.chunks, k)
            elif vector is True:
                sources = ind.vector_search(
                    loads.embedding, query, loads.chunks, k)
            else:
                if bm25_scores:
                    sources = ind.fetch_query_chunks(bm25_scores, k)
            return Response({
                "resources": [src.model_dump() for src in sources]
            })
        except (Exception, UsageError) as e:
            return Response({
                "error": e.__str__()
            },status=status.HTTP_404_NOT_FOUND)
        
    @staticmethod
    @api_view(['POST'])
    def search_dataset(req) -> Response:
        try:
            vector: bool | None = Controller.validate_flags(
                ('vector', req.data.get('vector'))
            )
            hybrid: bool | None = Controller.validate_flags(
                ('hybrid', req.data.get('hybrid'))
            )
            k: int = Controller.validate_numeric(
                ('k', req.data.get('k'), 1)
            ) or 5
            dataset: Dict[str, List[dict]] = Controller.validate_dataset(
                ('dataset', req.data.get('dataset'))
            )
            if (not dataset.get('rag_questions')):
                raise UsageError("given dataset doesnt contain rag_questions")
            if (vector is True and hybrid is True):
                raise UsageError("must use only one flag ['vector' | 'hybrid']")

            if (hybrid is True):
                indexer: HybridIndexer = HybridIndexer()
            elif vector is True:
                indexer: VectorIndexer = VectorIndexer()
            else:
                indexer: LexicalIndexer = LexicalIndexer()
            loads: Optional[BM25Index] = indexer.load(indexer.dest)
            if (not loads):
                ctr.index(indexer.dest.parent, hybrid, vector)
                return Controller.search_dataset(req)
            if (hybrid is True or vector is True) and loads.embedding is None:
                raise UsageError("embeddings are not founded on index file")
            dest: Path = indexer.search_multy(dataset, loads, k)
            data: Dict[str, str | list] = ctr.fetch_json(dest)
            os.remove(dest)
            return Response(data, status=status.HTTP_200_OK)

        except (Exception, UsageError) as e:
            return Response({
                "error": e.__str__()
            },status=status.HTTP_404_NOT_FOUND)
    
    @staticmethod
    @api_view(['POST'])
    def answer(req) -> Response:
        # def answer(query: str = '', k: int = 5, hybrid: str = '',
        #        path: Path = Path(''), vector: bool = '') -> None:
        try:
            vector: bool | None = Controller.validate_flags(
                ('vector', req.data.get('vector'))
            )
            hybrid: bool | None = Controller.validate_flags(
                ('hybrid', req.data.get('hybrid'))
            )
            k: int = Controller.validate_numeric(
                ('k', req.data.get('k'), 1)
            ) or 5
            query: str = Controller.validate_record(
                ('query', req.data.get('query'))
            )
            if (vector is True and hybrid is True):
                raise UsageError("must use only one flag ['vector' | 'hybrid']")

            if (hybrid is True):
                ind: HybridIndexer = HybridIndexer()
            elif (vector is True):
                ind: VectorIndexer = VectorIndexer()
            else:
                ind: LexicalIndexer = LexicalIndexer()
            loads: Optional[BM25Index] = ind.load(ind.dest)
            if (not loads):
                ctr.index(ind.dest.parent, hybrid, vector)
                return Controller.search(req._request)
            if (hybrid is True or vector is True) and loads.embedding is None:
                raise UsageError("embeddings are not founded on index file")

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
            return Response({
                "answer": res['generated_text']
            }, status=status.HTTP_200_OK)

        except (BaseException, UsageError) as e:
            return Response({
                "error": e.__str__()
            }, status=status.HTTP_404_NOT_FOUND)
    
    @staticmethod
    @api_view(['POST'])
    def answer_dataset(req) -> Response:
        #  def answer_dataset(student_search_results_path: str = '',
        #                save_directory: str = '',
        #                path: Path = Path('')):
        try:
            src: dict = Controller.validate_dataset(
                ('search_results', req.data)
            )
            if len(src.get('search_results')) == 0:
                return Response
            try:
                obj: StudentSearchResults = StudentSearchResults.model_validate(
                    src
                )
            except ValidationError as e:
                err: ErrorDetails = e.errors()[0]
                raise DataValidation(f"{err['type']} {err['loc'][0]}, {err['msg']}"
                                    + " on data source")
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
            return Response(res.model_dump(), status=status.HTTP_200_OK)

        except (BaseException, UsageError, DataValidation) as e:
            return Response({
                "error": e.__str__()
            }, status=status.HTTP_404_NOT_FOUND)
        

    @staticmethod
    @api_view(['POST'])
    def test(req):
        validator = SearchSerializer(data=req.data)
        if not validator.is_valid():
            print(validator.errors)
        else:
            print("all done")
            print(validator._validated_data)
        return Response({
            "body": "done"
        })