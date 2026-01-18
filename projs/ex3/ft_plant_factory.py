#!/usr/bin/python3
class Plant:
    """
    Represents a plant instance created by the factory.

    Attributes
    ----------
    count : int
        Class-level counter tracking the number of Plant instances created.
    name : str
        Name of the plant.
    height : int
        Height of the plant in centimeters.
    age : int
        Age of the plant in days.
    """
    count = 0

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant instance and increment the global plant counter.

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
        Plant.count += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory(data: list) -> list:
    """
    Create multiple Plant instances from structured input data.

    Parameters
    ----------
    data : list
        A list of dictionaries containing plant attributes.

    Returns
    -------
    list
        A list of created Plant instances.
    """
    re = []
    for plant in data:
        re.append(Plant(plant["name"], plant["height"], plant["age"]))
    return re


def main() -> None:
    """
    Initialize plant data, create Plant objects, and display statistics.
    """
    print("=== Plant Factory Output ===w")
    data = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120},
        ]
    ft_plant_factory(data)
    print("")
    print(f"Total plants created: {Plant.count}")


if __name__ == "__main__":
    main()
