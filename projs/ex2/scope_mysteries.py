from typing import Any, Union


def mage_counter() -> callable:
    x = 0

    def counter() -> int:
        nonlocal x
        x += 1
        return x
    return counter


def spell_accumulator(initial_power: int) -> callable:
    x = initial_power

    def accumilate(pw: int = 0) -> int:
        nonlocal x
        x += pw
        return x
    return accumilate


def enchantment_factory(enchantment_type: str) -> callable:
    def re(n: str) -> str:
        return f"{enchantment_type} {n}"
    return re


def memory_vault() -> dict[str, callable]:
    database = {}

    def store(key: Union[str, tuple, int, ], val: Any) -> None:
        print("called")
        if isinstance(key, (list, dict)):
            print("true")
        nonlocal database
        # database[key] = val

    def recall() -> Any:
        pass

    return {
        'store': store,
        'recall': recall
    }

mem = memory_vault()
mem['store'](2, "ahcraf")


