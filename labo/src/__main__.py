from src.chunker import Chunker
from src.indexer import Indexer
from typing import List
from src.error import UsageError, Error
import fire
import sys
from pathlib import Path
from functools import partial
def hints():
    print("Usage: ...")

def index(path: Path, max_chunk_size: int = 2000) -> None:
    if (isinstance(max_chunk_size, str) and not max_chunk_size.isnumeric()):
        raise UsageError(f"arg '{max_chunk_size}' is not an integer")

    chunker = Chunker(str(path / 'raw'), str(path / 'process'))
    cnk_path = chunker.discover_files().chunk()
    indexer = Indexer(str(path / 'process'))
    idx_path = indexer.tokenize_chunks(str(cnk_path))

def search(query: str = '', path: Path = Path(''), k: int = 5) -> None:
    if (query == ''):
        raise UsageError("missing 1 required positional argument 'qeury'")
    if (isinstance(k, str) and not k.isnumeric()):
        raise UsageError(f"arg '{k}' is not an integer")

    ind: Indexer = Indexer(str(path / 'process'))
    loads = ind.load(str(ind.dest))
    scores = ind.search(ind.split(query), loads)
    ind.fetch_query_chunks(scores, k)

def search_dataset(dataset_path: str = '', k: int = 5, save_directory: str = '', path: Path = Path('')):
    if (dataset_path == True or not dataset_path):
            raise UsageError("missing 1 required positional argument 'dataset_path'")
    if (save_directory == True or not save_directory):
            raise UsageError("missing 1 required positional argument 'save_directory'")
    if (isinstance(k, str) and not k.isnumeric()):
        raise UsageError(f"arg '{k}' is not an integer")
    src = Path(dataset_path)
    if (not src.exists()):
         raise FileNotFoundError(f"file not found '{src}'")
    


def main():
    data_path = Path("data")
    try:
        allowed_actions: List[str] = [
            'index', 'search', 'search_dataset', 'answer',
            'answer_dataset', 'evaluate'
            ]
        if (len(sys.argv) == 1):
            raise UsageError("not enough args")

        if sys.argv[1].strip().lower() not in allowed_actions:
            raise UsageError(f"unknown action '{sys.argv[1]}'")
    
        fire.Fire({
            "index": partial(index, path=data_path),
            "search": partial(search, path=data_path),
            "search_dataset": partial(search_dataset, path=data_path)
        })
    except UsageError as e:
        print(f"{e.__class__.__name__}: {e}")
        hints()
        sys.exit(1)
    except BaseException as e:
        print(f"{e.__class__.__name__}: {e}")
        sys.exit(1)



main()

