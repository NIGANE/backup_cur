import sys
from src.models.Parser import Parser


def main() -> None:
    parsed_data = Parser(sys.argv)
