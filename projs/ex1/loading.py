import importlib as lb


def module_not_found(name: str) -> None:
    print(f"Error: missing dependency: {name}")
    print(f"try install the ({name}):".capitalize())
    print(" - using 'pip' run:")
    print('\t|')
    print(f"\t|-- pip install {name}")
    print()
    print(" - using 'poetry' run:")
    print('\t|')
    print(f"\t|-- poetry add {name}")


def make_the_work() -> None:
    print()
    print("Analyzing Matrix data...")


def main() -> None:
    imports = ["pandas", 'requests', 'matplotlib']
    print()
    print("LOADING STATUS: Loading programs...")
    print()

    def module_uses(name: str) -> str:
        match name:
            case "pandas":
                return "Data manipulation ready"
            case "requests":
                return "Network access ready"
            case "matplotlib":
                return "Visualization ready"
            case _:
                return ""

    err = 0
    for ele in imports:
        try:
            module = lb.import_module(ele)
        except ModuleNotFoundError as e:
            err = 1
            module_not_found(e.name)
            return
        else:
            print(
                f"[OK] {module.__name__} ({module.__version__})"
                f" - {module_uses(ele)}"
                )

    if not err:
        make_the_work()


main() if __name__ == "__main__" else ""
