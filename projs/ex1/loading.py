import importlib as lb

modules = []


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


def handle_data(pd, res, mtlib):
    print()
    print("Analyzing Matrix data...")
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    data = None
    try:
        data = res.get(url)
        if data.status_code == 400:
            raise ValueError("end point has some issues".capitalize())
    except ValueError as e:
        print(e)
    df = pd.DataFrame(data.json())
    df = df[
        [
            "name",
            "symbol",
            "current_price",
            "market_cap",
            "total_volume",
            "price_change_percentage_24h"
        ]
    ]
    df = df[df["symbol"] != "btc"]
    df = df.head(20)
    print(df)
    plt = lb.import_module('matplotlib.pyplot')
    plt.figure(figsize=(15, 7))
    plt.bar(df["name"], df["current_price"])
    plt.xticks(rotation=90)
    plt.ylabel("USD")
    plt.title("Current Crypto Prices")
    plt.tight_layout()
    plt.show()


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
    i = 0
    for ele in imports:
        try:
            modules.append(lb.import_module(ele))
        except ModuleNotFoundError as e:
            err = 1
            module_not_found(e.name)
            return
        else:
            print(
                f"[OK] {modules[i].__name__} ({modules[i].__version__})"
                f" - {module_uses(ele)}"
                )
        finally:
            i += 1

    if not err and len(modules) == 3:
        pd, res, mtlib = modules
        handle_data(pd, res, mtlib)


main() if __name__ == "__main__" else ""
