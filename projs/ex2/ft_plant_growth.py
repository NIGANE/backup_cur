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
        self.age = age


def grow(pl: type[Plant]):
    """
        Increase the height of a plant by one centimeter.

        Parameters
        ----------
        pl : Plant
            The plant to grow.
    """
    pl.height += 1


def age(pl: type[Plant]):
    """
        Increase the age of a plant by one day.

        Parameters
        ----------
        pl : Plant
            The plant whose age will be incremented.
    """
    pl.age += 1


def get_info(pl: type[Plant]):
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
    return f"{pl.name}: {pl.height}cm, {pl.age} days old"


def main():
    """
      Simulate one week of plant growth and display results.
    """
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
