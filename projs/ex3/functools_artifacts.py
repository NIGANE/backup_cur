from typing import Any, Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    for ele in spells:
        if not isinstance(ele, int):
            raise ValueError(
                f"Unsuported operand ({type(ele).__name__}) "
                f"type for {operation}")
    match operation:
        case "add":
            return reduce(add, spells)
        case "multiply":
            return reduce(mul, spells)
        case "max":
            return reduce(max, spells)
        case "min":
            return reduce(min, spells)
    raise ValueError(f"none defined operation '{operation}'")


def partial_enchanter(base_enchantment: Callable) -> dict[str, partial]:
    my_dict = {}

    my_dict['fire_enchant'] = partial(
        base_enchantment, 50, 'fire_enchant')
    my_dict['ice_enchant'] = partial(
        base_enchantment, 50, 'ice_enchant')
    my_dict['lightning_enchant'] = partial(
        base_enchantment, 50, 'lightning_enchant')
    return my_dict


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def dispatch(n: Any) -> Any:
        return n

    @dispatch.register(int)
    def damage_spell(n: int) -> int:
        return n - 1

    @dispatch.register(list)
    def multi_cast(n: list) -> None:
        for ele in n:
            print(f"cast: {ele}")

    @dispatch.register(str)
    def enchantment(s: str) -> str:
        return f"enchantement {s}"
    return dispatch


# def enchanter(pw, ele, tar):
#     print(f"{ele} attack {tar} with {pw} power points")


def main() -> None:
    print()
    print("Testring spell reducer...")
    data = [40, 30, 20, 10]
    sum = spell_reducer(data, "add")
    print("Sum: ", sum)

    print("Product: ")

    max = spell_reducer(data, "max")
    print("Max: ", max)
    print()

    print("Testing momoized fibonacci...")
    print("FIB(10): ", memoized_fibonacci(10))
    print("FIB(15): ", memoized_fibonacci(15))


main() if __name__ == "__main__" else None
