#!/usr/bin/python3
class GardenManager:
    """
    Manages a garden and its plants.

    Tracks plant additions, growth, and provides reports
    about the garden's contents and statistics.

    Class Attributes
    ----------------
    total_gardens : int
        Total number of GardenManager instances created.
    """

    class GardenStats:

        @classmethod
        def plant_type(cls, owner: 'GardenManager') -> None:
            """
            Display a count of plant types in a garden.

            Parameters
            ----------
            owner : GardenManager
                The garden manager whose plants are analyzed.
            """
            data = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            for plant in owner.get_plants():
                if isinstance(plant, PrizeFlower):
                    data["PrizeFlower"] += 1
                elif isinstance(plant, FloweringPlant):
                    data["FloweringPlant"] += 1
                elif isinstance(plant, Plant):
                    data["Plant"] += 1

            print(
                f"Plant types: {data['Plant']} regular,"
                f" {data['FloweringPlant']} flowering,"
                f" {data['PrizeFlower']} prize flowers"
            )

        @staticmethod
        def get_total_gardens(cls: type['GardenManager']):
            """
            Return the total number of gardens managed.

            Returns
            -------
            str
                A formatted summary of total gardens.
            """
            return f"Total gardens managed: {cls.total_gardens}"

    total_gardens = 0

    @staticmethod
    def title() -> None:
        """
        Return the demo title banner.

        Returns
        -------
        str
            A formatted title string.
        """
        return "=== Welcome to the Garden Manager Demo ===\n"

    def __init__(self, owner: str, score: int) -> None:
        """
        Initialize a GardenManager instance.

        Parameters
        ----------
        owner : str
            Name of the garden owner.
        score : int
            Score associated with the garden.
        """
        self.__owner = owner
        self.__plants = []
        self.__count = 0
        self.__total_growth = 0
        self.__score = score
        GardenManager.total_gardens += 1

    def get_owner(self) -> None:
        """
        Get the formatted owner name.

        Returns
        -------
        str
            Owner name in title case.
        """
        return self.__owner.title()

    def get_plants(self) -> None:
        """
        Retrieve all plants in the garden.

        Returns
        -------
        list
            List of plant objects.
        """
        return self.__plants

    def get_garden_score(self) -> None:
        """
        Get the garden's score.

        Returns
        -------
        int
            Garden score.
        """
        return self.__score

    def info(self) -> None:
        """
        Return a summary of garden activity.

        Returns
        -------
        str
            Information about plant count and growth.
        """
        return (
            f"Plant added: {self.__count},"
            f"Total growth: {self.__total_growth}cm"
        )

    def report(self) -> None:
        """
        Print a detailed report of the garden contents.
        """
        print(f"=== {self.__owner.title()}'s Garden Report ===")
        print("Plants in the garden:")
        for plant in self.__plants:
            print(plant.describe())

    def add_plant(self, *plants: 'Plant') -> None:
        """
        Add one or more plants to the garden.

        Parameters
        ----------
        *plants : Plant
            Variable number of plant objects to add.
        """
        for plant in plants:
            self.__plants.append(plant)
            self.__count += 1
            print(
                f"Added {plant.get_name()} to "
                f"{self.__owner.title()}'s garden"
            )

    def plants_grow(self) -> None:
        """
        Trigger growth for all plants in the garden.
        """
        print(f"{self.__owner.title()} is helping all plants grow...")
        for plant in self.__plants:
            plant.grow()
            self.__total_growth += 1

    def height_test(self) -> None:
        """
        Check whether total plant height is greater than zero.

        Returns
        -------
        bool
            True if cumulative height is positive, otherwise False.
        """
        height = 0
        for plant in self.__plants:
            height += plant.get_height()
        return height > 0


class Plant:
    """
    Represents a basic plant.

    Attributes
    ----------
    name : str
        Name of the plant.
    height : int
        Height of the plant in centimeters.
    """

    def __init__(self, name: str, height: int) -> None:
        """
        Initialize a Plant instance.

        Parameters
        ----------
        name : str
            Name of the plant.
        height : int
            Initial height in centimeters.
        """
        self.__name = name
        self.__height = height

    def get_name(self) -> None:
        """
        Get the plant name.

        Returns
        -------
        str
            Plant name.
        """
        return self.__name

    def get_height(self) -> None:
        """
        Get the plant height.

        Returns
        -------
        int
            Plant height in centimeters.
        """
        return self.__height

    def grow(self, height: int = 1) -> None:
        """
        Increase the plant's height.

        Parameters
        ----------
        height : int, optional
            Growth increment in centimeters (default is 1).
        """
        self.__height += height
        print(f"{self.__name.title()} grew {height}cm")

    def describe(self) -> None:
        """
        Describe the plant.

        Returns
        -------
        str
            Description including name and height.
        """
        return f"- {self.__name.title()}: {self.__height}cm"


class FloweringPlant(Plant):
    """
    Represents a flowering plant.

    Inherits from
    -------------
    Plant
    """

    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Initialize a FloweringPlant instance.

        Parameters
        ----------
        name : str
            Name of the plant.
        height : int
            Height in centimeters.
        color : str
            Flower color.
        """
        super().__init__(name, height)
        self.__color = color

    def describe(self) -> str:
        """
        Describe the flowering plant.

        Returns
        -------
        str
            Description including flower color.
        """
        return super().describe() + f", {self.__color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """
    Represents a prize-winning flowering plant.

    Inherits from
    -------------
    FloweringPlant
    """

    def __init__(
            self, name: str, height: int, color: str, points: int
            ) -> None:
        """
        Initialize a PrizeFlower instance.

        Parameters
        ----------
        name : str
            Name of the plant.
        height : int
            Height in centimeters.
        color : str
            Flower color.
        points : int
            Prize points awarded.
        """
        super().__init__(name, height, color)
        self.__points = points

    def describe(self) -> str:
        """
        Describe the prize flower.

        Returns
        -------
        str
            Description including prize points.
        """
        return super().describe() + f", Prize points: {self.__points}"


def add_plants_to_garden(garden: GardenManager, *plants: Plant) -> None:
    for e in plants:
        garden.add_plant(e)


def main() -> None:
    """
    Run the Garden Manager demonstration.
    """
    print(GardenManager.title())

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "Red")
    sunflower = PrizeFlower("Sunflower", 50, "Yellow", 10)

    alice = GardenManager("alice", 218)
    bob = GardenManager("bob", 92)

    add_plants_to_garden(alice, oak, rose, sunflower)
    print("")

    alice.plants_grow()
    print("")

    alice.report()
    print("")
    print(alice.info())

    GardenManager.GardenStats.plant_type(alice)
    print("")

    print(f"Height validation test: {alice.height_test()}")
    print(
        f"Garden scores - "
        f"{alice.get_owner()}: {alice.get_garden_score()},"
        f" {bob.get_owner()}: {bob.get_garden_score()}"
    )

    print(GardenManager.GardenStats.get_total_gardens(GardenManager))


if __name__ == "__main__":
    main()
