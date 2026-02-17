from typing import Any


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    if callable(spell1) and callable(spell2):
        def fun(*args: Any, **d: Any) -> tuple:
            return (spell1(*args, **d), spell2(*args, **d))
        return fun
    if callable(spell1) and not callable(spell2):
        return spell1
    elif callable(spell2) and not callable(spell1):
        return spell2
    else:
        raise (ValueError(f"{spell1} ({type(spell1).__name__}) and "
                          f"{spell2} ({type(spell2).__name__}) "
                          f"are not callable"))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    if (not callable(base_spell)):
        raise ValueError(f"{base_spell} "
                         f"({type(base_spell)}) is not a callable")

    return lambda: base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    if (not callable(condition) or not callable(spell)):
        raise ValueError(f"args ({condition} and {spell}) "
                         f"must be of type callable")

    def tty(*args: Any, **ke: Any) -> Any:
        if condition(*args, **ke):
            return spell(*args, **ke)
        else:
            return "Spell fizzled"
    return tty


def spell_sequence(spells: list[callable]) -> callable:
    for ele in spells:
        if not callable(ele):
            raise ValueError(f"{ele} ({type(ele)}) is not callable")

    def cast(*ar: Any, **av: Any) -> Any:
        re = []
        for ele in spells:
            if (ar and av):
                re.append(ele(*ar, av))
            elif ar:
                re.append(ele(*ar))
            elif av:
                re.append(ele(av))
            else:
                re.append(ele())
        return re
    return cast


def main() -> None:
    print()
    print("Testing spell combiner...")
    comb = spell_combiner(
        lambda: "Fireball hits Dragon", lambda: "Heals Dragon")
    re = comb()
    print(f"Combined spells result: {re[0]}, {re[-1]}")
    print()

    print("Testing power amplifier...")
    print(f"original: {10}, Amplified: {power_amplifier(lambda: 10, 3)()}")


if __name__ == "__main__":
    main()
