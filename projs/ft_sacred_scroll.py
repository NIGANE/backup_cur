import alchemy


def main():
    print()
    print("=== Sacred Scroll Mastery ===")
    print()

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}"
        )
    print(
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}"
        )
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")
    print()

    print("Testing package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")
    print()

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
