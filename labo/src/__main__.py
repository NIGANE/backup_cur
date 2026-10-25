from typing import List
from src.error import UsageError, Error, DataValidation
import fire
import sys
from pathlib import Path
from functools import partial
from src.controller import Controller as ctr
from pydantic import ValidationError

def hints():
    print("Usage: ...")    


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
            "index": partial(ctr.index, path=data_path),
            "search": partial(ctr.search, path=data_path),
            "search_dataset": partial(ctr.search_dataset, path=data_path),
            "answer": partial(ctr.answer, path=data_path),
            "answer_dataset": partial(ctr.answer_dataset, path=data_path)
        })
    except UsageError as e:
        print(f"{e.__class__.__name__}: {e}")
        hints()
        sys.exit(1)
    except DataValidation as e:
        print(f"{e.__class__.__name__}: {e}")
    except BaseException as e:
        print(f"{e.__class__.__name__}: {e}")
        sys.exit(1)



main()

