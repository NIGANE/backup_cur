from typing import Any


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

    def store(key: Any, val: Any) -> None:
        if (isinstance(key, (list, dict, set))):
            raise ValueError(
                f"could not accept {type(key).__name__} as key for dict type")
        nonlocal database
        database[key] = val

    def recall(key: Any) -> Any:
        if (isinstance(key, (list, dict, set))):
            raise ValueError(
                f"could not accept {type(key).__name__} as key for dict type")
        return database.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print()
    print("Testing mage counter...")
    cn = mage_counter()
    for e in range(1, 4):
        print("Call ", e, ": ", cn())
    print()

    print("Testing enchantment factory...")
    falmin = enchantment_factory("Falming")
    falmin_clone = falmin("Sword")
    print(falmin_clone.title())

    frozen = enchantment_factory("Frozen")
    frozen_clone = frozen("Shield")
    print(frozen_clone.title())


main() if __name__ == "__main__" else None
