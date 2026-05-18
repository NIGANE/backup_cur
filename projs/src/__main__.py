import sys
from src.prompting import prompting
from src.parse import error_usage_func
from src.parse import parse



def main():
    if (len(sys.argv) < 7):
        error_usage_func()
    valid_data = parse()
    prompting()


if __name__ == "__main__":
    main()
