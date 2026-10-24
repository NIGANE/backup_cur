from pathlib import Path
import json
from src.error import Error
from typing import Dict, List, Optional
from src.chunker import Chunker
from src.indexer import Indexer, BM25Index
from src.error import Error, UsageError
from src.models import MinimalSearchResults
from transformers import pipeline

class Controller:
    def __init__(self):
        pass

    @staticmethod
    def fetch_json(path: Path) -> Dict[str, List[Dict[str, str]]]:
        if (not path.exists()):
            raise FileNotFoundError(f"file not found '{path}'")
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise Error(e)

    @staticmethod
    def inference(contexts: List[str], query: str, model: str = 'Qwen/Qwen3-0.6B'):
        generator = pipeline(
            'text-generation',
            model=model,
            device='cpu'
            )
        context: str = "\n\n".join([
            f"- chunk: {ch}" for ch in contexts
        ])
        prompt = f"""Use the context below to answer the question.

        Context:
        {context}

        Question: {query}
        Answer:"""
        res = generator(
            prompt,
            max_new_tokens=50,
            do_sample=False,        # greedy = more deterministic
            return_full_text=False 
        )
        return (res[0]['generated_text'])

    @staticmethod
    def index(path: Path, max_chunk_size: int = 2000) -> None:
        if (isinstance(max_chunk_size, str) and not max_chunk_size.isnumeric()):
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

        scores = ind.search(query, loads)
        ind.fetch_query_chunks(scores, k)
        for source in ind.last_resolved:
            print(f"{source.file_path} [{source.first_character_index}:{source.last_character_index}]")



    @staticmethod
    def search_dataset(dataset_path: str = '', k: int = 5, save_directory: str = '', path: Path = Path('')):
        if (dataset_path == True or not dataset_path):
                raise UsageError("missing 1 required positional argument 'dataset_path'")
        if (save_directory == True or not save_directory):
                raise UsageError("missing 1 required positional argument 'save_directory'")
        if (isinstance(k, str) and not k.isnumeric()):
            raise UsageError(f"arg '{k}' is not an integer")
        if (isinstance(k, bool)):
            raise UsageError("missing 1 optional argument value '--k'?")
        src = Path(dataset_path)
        data: Dict[str, List[Dict[str, str]]] = Controller.fetch_json(src)
        if (not data):
            raise UsageError(f"the feeded file is empty '{src}'")
        indexer = Indexer(save_directory)
        loads: Optional[BM25Index] = indexer.load(path / 'process')
        if (not loads):
            Controller.index(path)
            return Controller.search_dataset(dataset_path, k, save_directory, path)
        dest = indexer.search_multy(data, loads, k)
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

        context: List[str] = []
        for e in ind.last_resolved:
            re = Chunker.get_chunk(e)
            context.append(re)
        res = Controller.inference(context, query)
        print(res)
