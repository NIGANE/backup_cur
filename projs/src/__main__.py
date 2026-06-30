import sys
from typing import List
from src.models.Parser import Parser
from src.models.Error import MyError
from src.models.Manager import Manager


def _usage() -> str:
    return "usage :uv run python -m src <FILE_PATH>"


def main() -> None:

    try:
        if (len(sys.argv) != 2):
            raise MyError(f"Error: {_usage()}")
        parser: Parser = Parser(sys.argv)
        data: List[str] = parser.load_file()
        manager: Manager = parser.run_validation(data)
        manager.path_finding()
        manager.run_simulation()
    except MyError as e:
        print(f"# {e}")
    # except BaseException as e:
    #     print(f"external Error ({e.__class__.__name__}): {e}")


if __name__ == "__main__":
    main()
