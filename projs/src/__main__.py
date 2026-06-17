import sys
from src.models.Parser import Parser
from src.models.Error import MyError


def _usage() -> str:
    return "usage :uv run python -m src <FILE_PATH>"


def main() -> None:

    try:
        if (len(sys.argv) != 2):
            raise MyError(f"Error: {_usage()}")
        parsed_data = Parser(sys.argv)
    except MyError as e:
        print(f"# {e}")
    # except BaseException as e:
    #     print(f"external Error ({e.__class__.__name__}): {e}")



if __name__ == "__main__":
    main()
