from functools import wraps
from datetime import datetime
from typing import Any, Callable
import time


def spell_timer(func: Callable) -> Callable:
    if (not callable(func)):
        raise ValueError(f"expected Callable not {type(func).__name__}")

    @wraps(func)
    def wp(*ar: Any, **key: Any) -> Any:
        print(f"Casting {func.__name__}...")
        st = datetime.now()
        re = func(*ar, **key)
        end = datetime.now()
        print(
            f"Spell completed in "
            f"{float((end - st).total_seconds()):.3f} seconds"
            )
        return re
    return wp


def power_validator(min_power: int) -> Callable:
    def decorator(fn: Callable) -> Callable:
        def wp(*ar: Any, **key: Any) -> Any:
            pw = key.get('power', min_power - 1)
            if (isinstance(pw, int) and pw >= min_power):
                return fn(*ar, **key)
            else:
                return "Insufficient power for this spell"
        return wp
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decor(fn: Callable) -> Callable:
        def wp(*ar: Any, **key: Any) -> Any:
            for tr in range(1, max_attempts):
                try:
                    re = fn(*ar, **key)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {tr}/{max_attempts})"
                        )
                else:
                    return re
            return f"Spell casting failed after {max_attempts} attempts"
        return wp
    return decor


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for c in name.lower():
                if c not in "abcdefghijklmnopqrstuvwxyz ":
                    return False
            return True
        return False

    @power_validator(10)
    def cast_spell(s, spell_name: str, power: int) -> str:
        return ("Successfully cast "
                f"{spell_name.capitalize()} with {power} power")


def main() -> None:
    print()

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    print("Testing spell timer")
    print("Result:", fireball())
    print()

    print("Testing MageGuid...")
    print(MageGuild.validate_mage_name("Dragon "))
    print(MageGuild.validate_mage_name("shild 2"))

    print(MageGuild().cast_spell('Lightning', power=15))
    print(MageGuild().cast_spell('Lightning', power=9))


main() if __name__ == '__main__' else None
