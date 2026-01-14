class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def grow(pl: type[Plant]):
    pl.height += 1

def age(pl: type[Plant]):
    pl.age += 1

def get_info(pl: type[Plant]):
    return f"{pl.name}: {pl.height}cm, {pl.age} days old"
    

def main():
    print("=== Day 1 ===")
    rosee = Plant("rose", 25, 30)
    print(get_info(rosee))
    i = 1
    print("=== Day 7 ===")
    while (i < 7):
        grow(rosee)
        age(rosee)
        i += 1
    print(get_info(rosee))
    print(f"Growth this week: +{rosee.height - 25}cm")


if __name__ == "__main__":
    main()
