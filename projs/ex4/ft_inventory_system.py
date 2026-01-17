import sys


def ne_sum(data: list[int]) -> int:
    re = 0
    for e in data:
        re += e
    return re


def ne_count(data: list[int]) -> int:
    re = 0
    for e in {*data}:
        re += 1
    return re


def ne_max(data: dict[str, int]) -> str:
    item = ""
    max = data[[*data][0]]
    for key, value in data.items():
        if (value >= max):
            max = value
            item = key
    return item


def ne_min(data: dict[str, int]) -> str:
    item = ""
    min = data[[*data][0]]
    for key, value in data.items():
        if (value <= min):
            min = value
            item = key
    return item


def round(value: int, data: dict[str, int]) -> int:
    return (value / ne_sum([ele for ele in data.values()]) * 100)


def parsing_args(data: list[str]) -> dict[str, int]:
    re = dict()
    try:
        for ele in data:
            re[ele.split(":")[0]] = int(ele.split(":")[1])
    except ValueError as e:
        print(e)
    else:
        return re


def ft_inventory_system() -> None:
    args = sys.argv
    if (len(args) > 1):
        print("=== Inventory System Analysis ===")
        data = parsing_args(args[1:])
        if (data is not None):
            print(
                f"Total items in inventory: "
                f"{ne_sum([ele for ele in data.values()])}"
                )
            print(f"Unique item types: {ne_count(ele for ele in data.keys())}")
        print("")
        print("=== Current Inventory ===")
        for key, value in data.items():
            print(
                f"{key}: {value} {'units' if value > 1 else 'unit'} "
                f"({round(value, data):.1f}%)"
                )
        print("")
        print("=== Inventory Statistics ===")
        print(f"Most abundant: {ne_max(data)} ({data[ne_max(data)]} units)")
        print(
            f"Least abundant: {ne_min(data)} ({data[ne_min(data)]} "
            f"{'units' if data.get(ne_min(data), 0) >= 2 else 'unit'})"
            )
        print("")
        print("=== Item Categories ===")


if __name__ == "__main__":
    ft_inventory_system()
