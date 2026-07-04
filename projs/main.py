import sys
from typing import List
from Parser import Parser
from Error import MyError
from Manager import Manager


def _usage() -> str:
    """Return the command-line usage message.

    Returns:
        A string describing the expected command-line syntax.
    """
    return "usage :uv run python -m src <FILE_PATH>"


def main() -> None:
    """Run the application.

    Validates the command-line arguments, loads and validates the input
    file, computes the path, and executes the simulation. Any application
    errors are reported with a user-friendly message, while unexpected
    exceptions are reported separately.
    """
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
    except BaseException as e:
        print(f"external Error ({e.__class__.__name__}): {e}")


if __name__ == "__main__":
    main()
