#!/usr/bin/python3
import sys


def ne_sum(data: list[int]) -> int:
    """Calculates the total sum of all integer values in a list."""
    re = 0
    for e in data:
        re += e
    return re


def ne_count(data: list[int]) -> int:
    """Counts the number of unique types present in the data."""
    re = 0
    for e in {*data}:
        re += 1
    return re


def ne_max(data: dict[str, int]) -> str:
    """Finds the key with the highest integer value in the dictionary."""
    item = ""
    max = data[[*data][0]]
    for key, value in data.items():
        if (value >= max):
            max = value
            item = key
    return item


def ne_min(data: dict[str, int]) -> str:
    """Finds the key with the lowest integer value in the dictionary."""
    item = ""
    min = data[[*data][0]]
    for key, value in data.items():
        if (value <= min):
            min = value
            item = key
    return item


def round(value: int, data: dict[str, int]) -> int:
    """
    Calculates what percentage a specific value is of the total inventory sum.
    """
    return (value / ne_sum([ele for ele in data.values()]) * 100)


def modern(data: dict[str, int]) -> dict[str, int]:
    """
    Filters inventory for items with a 'moderate' stock level (5 or more).
    """
    re = dict()
    for e, v in data.items():
        if v >= 5:
            re[e] = v
    return re


def scare(data: dict[str, int]) -> dict[str, int]:
    """
    Filters inventory for items with a 'scarce' stock level (less than 5).
    """
    re = dict()
    for e, v in data.items():
        if v < 5:
            re[e] = v
    return re


def needed(data: dict[str, int]) -> list[str]:
    """Identifies items that are at critical levels (exactly 1 unit)."""
    re = []
    for e, v in data.items():
        if v == 1:
            re = [*re, e]
    return re


def parsing_args(data: list[str]) -> dict[str, int]:
    """
    Parses a list of strings formatted as 'item:count' into a dictionary.

    Args:
        data: A list of strings (e.g., ['sword:5', 'shield:2']).

    Returns:
        A dictionary mapping item names (str) to their counts (int).
    """
    re = dict()
    try:
        for ele in data:
            re[ele.split(":")[0]] = int(ele.split(":")[1])
    except ValueError as e:
        print(e)
    else:
        return re


def ft_inventory_system() -> None:
    """
    Main execution flow for the inventory system.
    Processes CLI arguments and prints the analytics report.
    """
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
        print(f"Moderate: {modern(data)}")
        print(f"Scarce: {scare(data)}")
        print("")

        print("=== Management Suggestions ===")
        print(f"Restock needed: {needed(data)}")
        print("")

        print("=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {[*data.keys()]}")
        print(f"Dictionary values: {[*data.values()]}")
        print(
            f"Sample lookup - 'sword' in inventory: "
            f"{'sword' in [*data.keys()]}"
            )


if __name__ == "__main__":
    ft_inventory_system()
