from src.chunker import Chunker, Error
from src.indexer import Indexer
from typing import List
from src.error import UsageError
import fire
import sys
def hints():
    print("Usage: ...")

def index(max_chunk_size: int = 200):
    if (isinstance(max_chunk_size, str) and not max_chunk_size.isnumeric()):
        raise UsageError(f"UsageError: not real integer '{max_chunk_size}'")
    
def main():
    try:
        allowed_actions: List[str] = [
            'index', 'search', 'search_dataset', 'answer',
            'answer_dataset', 'evaluate'
            ]
        if (len(sys.argv) == 1):
            raise UsageError("UsageError: not enough args")

        if sys.argv[1].strip().lower() not in allowed_actions:
            raise UsageError(f"UsageError: unknown action '{sys.argv[1]}'")
    
        fire.Fire({
            "index": index
        })
    except UsageError as e:
        print(e)
        hints()
        sys.exit(1)
    except Error as e:
        print(e)

    # print(max_chunk_size)
    # try:
    #     allowed_actions: List[str] = [
    #         'index', 'search', 'search_dataset', 'answer',
    #         'answer_dataset', 'evaluate'
    #         ]
    #     if (len(sys.argv) == 1):
    #         raise UsageError("UsageError: not enough args")

    #     if sys.argv[1].strip().lower() not in allowed_actions:
    #         raise UsageError(f"UsageError: unknown action '{sys.argv[1]}'")

    #     if sys.argv[1].strip().lower() == 'index':
    #         index(sys.argv)
    #     sys.exit()
    #     user_query = "self"
    #     k = 2
    #     chunker = Chunker("test", "data/process")
    #     # cnk_path = chunker.discover_files().chunk()
    #     # indexer = Indexer("data/process")
    #     # idx_path = indexer.tokenize_chunks(str(cnk_path))

    #         # search
    #     # ind = Indexer("data/process")
    #     # loads = ind.load(str(ind.dest))
    #     # scores = ind.search(ind.split(user_query), loads)
    #     # ind.fetch_query_chunks(scores, k)
    # except UsageError as e:
    #     print(e)
    #     hints()
    #     sys.exit(1)
    # except Error as e:
    #     print(e)



main()