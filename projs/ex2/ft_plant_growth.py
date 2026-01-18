#!/usr/bin/python3
class Plant:
    """
        Represents a plant with growth-related attributes.

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
                Initial height of the plant in centimeters.
            age : int
                Initial age of the plant in days.
        """
        self.name = name
        self.height = height
        self.ag = age

    def grow(s) -> None:
        """
            Increase the height of a plant by one centimeter.
        """
        s.height += 1

    def age(s) -> None:
        """
            Increase the age of a plant by one day.

            Parameters
            ----------
            pl : Plant
                The plant whose age will be incremented.
        """
        s.ag += 1

    def get_info(pl) -> str:
        """
            Return a formatted string describing the plant.

            Parameters
            ----------
            pl : Plant
                The plant to describe.

            Returns
            -------
            str
                A string containing the plant name, height, and age.
        """
        return f"{pl.name}: {pl.height}cm, {pl.ag} days old"


def main():
    """
      Simulate one week of plant growth and display results.
    """
    print("=== Day 1 ===")
    rosee = Plant("rose", 25, 30)
    print(rosee.get_info())
    i = 1
    print("=== Day 7 ===")
    while (i < 7):
        rosee.grow()
        rosee.age()
        i += 1
    print(rosee.get_info())
    print(f"Growth this week: +{rosee.height - 25}cm")


if __name__ == "__main__":
    main()
