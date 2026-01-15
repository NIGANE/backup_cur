class Plant:
    """
    Base class representing a generic plant.

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


class Flower(Plant):
    """
    Represents a flowering plant.

    Inherits from
    -------------
    Plant

    Attributes
    ----------
    color : str
        Color of the flower.
    """

    def __init__(self, name: str, height: int, age: int, color: str):
        """
        Initialize a Flower instance.

        Parameters
        ----------
        name : str
            Name of the flower.
        height : int
            Height of the flower in centimeters.
        age : int
            Age of the flower in days.
        color : str
            Color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def describe(self):
        """
        Describe the flower.

        Returns
        -------
        str
            A message describing the flower's attributes.
        """
        return (
            f"{self.name.title()} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
            )

    def bloom(self):
        """
        Simulate the flower blooming.

        Returns
        -------
        str
            A message indicating the flower is blooming.
        """
        return (f"{self.name.title()} is blooming beautifully!")


class Tree(Plant):
    """
    Represents a tree.

    Inherits from
    -------------
    Plant

    Attributes
    ----------
    trunk_diameter : int
        Diameter of the tree trunk in centimeters.
    """
    def __init__(
            self, name: str, height: int, age: int,
            trunk_diameter: int, shade_area: int
            ):
        """
        Initialize a Tree instance.

        Parameters
        ----------
        name : str
            Name of the tree.
        height : int
            Height of the tree in centimeters.
        age : int
            Age of the tree in days.
        trunk_diameter : int
            Diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_area = shade_area

    def describe(self):
        """
        Describe the tree.

        Returns
        -------
        str
            A message describing the tree's attributes.
        """
        return (
            f"{self.name.title()} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
            )

    def produce_shade(self):
        """
        Describe the shade produced by the tree.

        Returns
        -------
        str
            A message describing the shade area.
        """
        return (
            f"{self.name.title()} provides {self.shade_area}"
            f" square meters of shade"
            )


class Vegetable(Plant):
    """
    Represents a vegetable plant.

    Inherits from
    -------------
    Plant

    Attributes
    ----------
    harvest_season : str
        Season during which the vegetable is harvested.
    nutritional_value : str
        Primary nutritional benefit of the vegetable.
    """

    def __init__(self, name: str, height: int, age: int, hs, nv: str):
        """
        Initialize a Vegetable instance.

        Parameters
        ----------
        name : str
            Name of the vegetable.
        height : int
            Height of the vegetable in centimeters.
        age : int
            Age of the vegetable in days.
        hs : str
            Harvest season.
        nv : str
            Nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season = hs
        self.nutritional_value = nv

    def describe(self):
        """
        Describe the vegetable.

        Returns
        -------
        str
            A message describing the vegetable's attributes.
        """
        return (
            f"{self.name.title()} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
            )

    def get_info(self):
        """
        Retrieve nutritional information about the vegetable.

        Returns
        -------
        str
            A message describing the vegetable's nutritional value.
        """
        return (
            f"{self.name.title()} is rich in "
            f"{self.nutritional_value.title()}"
            )


def create_flowers(
        name: str, height: int, age: int, color: str
        ) -> Flower:
    """
    Factory function to create a Flower instance.

    Parameters
    ----------
    name : str
        Name of the flower.
    height : int
        Height of the flower in centimeters.
    age : int
        Age of the flower in days.
    color : str
        Color of the flower.

    Returns
    -------
    Flower
        An instance of the Flower class.
    """
    return Flower(name, height, age, color)


def create_trees(
        name: str, height: int, age: int, trunk_diameter: int
        ) -> Tree:
    """
    Factory function to create a Tree instance.

    Parameters
    ----------
    name : str
        Name of the tree.
    height : int
        Height of the tree in centimeters.
    age : int
        Age of the tree in days.
    trunk_diameter : int
        Diameter of the trunk in centimeters.

    Returns
    -------
    Tree
        An instance of the Tree class.
    """
    return Tree(name, height, age, trunk_diameter)


def create_vegetables(
        name: str, height: int, age: int, hs: str, nv: str
        ) -> Vegetable:
    """
    Factory function to create a Vegetable instance.

    Parameters
    ----------
    name : str
        Name of the vegetable.
    height : int
        Height of the vegetable in centimeters.
    age : int
        Age of the vegetable in days.
    hs : str
        Harvest season.
    nv : str
        Nutritional value.

    Returns
    -------
    Vegetable
        An instance of the Vegetable class.
    """
    return Vegetable(name, height, age, hs, nv)


def main() -> None:
    """
    Entry point of the program.

    Creates and displays information about various plant types
    in a simulated garden environment.
    """

    def demo_flower():
        flower_1 = Flower("rose", 25, 30, "red")
        flower_2 = Flower("tulip", 30, 40, "purple")
        flower_2
        print(flower_1.describe())
        print(flower_1.bloom())

    def demo_tree():
        tree_1 = Tree("oak", 500, 1825, 50, 78)
        tree_2 = Tree("pine", 600, 4000, 100, 120)
        tree_2
        print(tree_1.describe())
        print(tree_1.produce_shade())

    def demo_vegetable():
        vegetable_1 = Vegetable("tomato", 80, 90, "summer", "vitami c")
        vegetable_2 = Vegetable("spinach", 50, 60, "winter", "iron")
        vegetable_2
        print(vegetable_1.describe())
        print(vegetable_1.get_info())

    print("=== Garden Plant Types ===")
    print("")
    demo_flower()
    print("")
    demo_tree()
    print("")
    demo_vegetable()


if __name__ == "__main__":
    main()
