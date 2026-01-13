
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def main():
    rosee = Plant("rose", 25, 30)
    Sunflower = Plant("sunflower", 80, 45)
    Cactus = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(f"{rosee.name}: {rosee.height}cm, {rosee.age} days old")
    print(f"{Sunflower.name}: {Sunflower.height}cm, {Sunflower.age} days old")
    print(f"{Cactus.name}: {Cactus.height}cm, {Cactus.age} days old")


if __name__ == "__main__":
    main()
