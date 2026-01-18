#!/usr/bin/python3
class Plant:
    """
        Represents a plant with basic attributes.

        Attributes
        ----------
        name : str
            Name of the plant.
        height : int
            Height of the plant in centimeters.
        age : int
            Age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int):
        """
            Initialize a Plant instance.

            Parameters
            ----------
            name : str
                Name of the plant.
            height : int
                Height of the plant in centimeters.
            age : int
                Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


def main():
    """
        Create plant instances and display their information.
    """
    rosee = Plant("rose", 25, 30)
    Sunflower = Plant("sunflower", 80, 45)
    Cactus = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(f"{rosee.name}: {rosee.height}cm, {rosee.age} days old")
    print(f"{Sunflower.name}: {Sunflower.height}cm, {Sunflower.age} days old")
    print(f"{Cactus.name}: {Cactus.height}cm, {Cactus.age} days old")


if __name__ == "__main__":
    main()
