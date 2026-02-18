from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, sub, pow, truediv, mul, floordiv, mod


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


def base_ench(power, element, target):
    print("power: ", power)
    print("ele: ", element)
    print("target: ", target)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
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

def spell_dispatcher() -> callable:
    @singledispatch
    def dispatch(n: Any) -> Any:
        return n

    @dispatch.register(int)
    def damage_spell(n: int) -> None:
        pass

    @dispatch.register(list)
    def multi_cast(n: list) -> None:
        return n.join()

    @dispatch.register(str)
    def enchantment(s: str) -> None:
        return f"enchantement {s}"
    return dispatch
dis = spell_dispatcher()
# print(dis(["hello", "world"]))
print(("hello", "world").join())