import alchemy.elements
from alchemy.elements import create_fire
from alchemy import healing_potion as heal
from alchemy.potions import create_earth, strength_potion, create_fire


def main() -> None:
    print()
    print("=== Import Transmutation Mastery ===")
    print()

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {create_fire()}")
    print()

    print("Method 2 - Specific function import:")
    print(f"create_water(): {alchemy.elements.create_water()}")
    print()

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")
    print()

    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire():{create_fire()}")
    print(f"strength_potion(): {strength_potion()}")
    print()

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
