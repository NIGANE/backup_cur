class GardenManager:
    total_gardens = 0

    @staticmethod
    def title():
        return ("=== Welcome to the Garden Manager Demo ===\n")

    @classmethod
    def plant_type(cls, owner: type['GardenManager']) -> None:
        data = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
        for plant in owner.get_plants():
            if isinstance(plant, PrizeFlower):
                data["PrizeFlower"] += 1
            elif isinstance(plant, FloweringPlant):
                data["FloweringPlant"] += 1
            else:
                data["Plant"] += 1
        print(
            f"Plant types: {data['Plant']} regular,"
            f" {data['FloweringPlant']} flowering,"
            f" {data['PrizeFlower']} prize flowers"
        )

    @classmethod
    def get_total_gardens(cls):
        return f"Total gardens managed: {cls.total_gardens}"

    def __init__(self, owner: str, score: int):
        self.__owner = owner
        self.__plants = []
        self.__count = 0
        self.__total_growth = 0
        self.__score = score
        GardenManager.total_gardens += 1

    def get_owner(self):
        return self.__owner.title()

    def get_plants(self):
        return self.__plants

    def get_garden_score(self):
        return self.__score

    def info(self):
        return f"Plant added: {self.__count}," + \
         f"Total growth: {self.__total_growth}cm"

    def report(self):
        print(f"=== {self.__owner.title()}'s Garden Report ===")
        print("Plants in the garden:")
        for plant in self.__plants:
            print(plant.describe())

    def add_plant(self, *plants: type['Plant']):
        for plant in plants:
            self.__plants.append(plant)
            self.__count += 1
            print(
                f"Added {plant.get_name()} to "
                f"{self.__owner.title()}'s garden"
                )

    def plants_grow(self):
        print(f"{self.__owner.title()} is helping all plants grow...")
        for plant in self.__plants:
            plant.grow()
            self.__total_growth += 1

    def height_test(self):
        height = 0
        for plant in self.__plants:
            height += plant.get_height()
        if height > 0:
            return True
        return False


class Plant():

    def __init__(self, name: str, height: int):
        self.__name = name
        self.__height = height

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def grow(self, height: int = 1):
        self.__height += height
        print(f"{self.__name.title()} grew {height}cm")

    def describe(self):
        return f"- {self.__name.title()}: {self.__height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.__color = color

    def describe(self):
        return super().describe() + f", {self.__color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.__points = points

    def describe(self):
        return super().describe() + f", Prize points: {self.__points}"


def main():
    print(GardenManager.title())
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "Red")
    sunflower = PrizeFlower("Sunflower", 50, "Yellow", 10)
    alice = GardenManager("alice", 218)
    bob = GardenManager('bob', 92)
    alice.add_plant(oak, rose, sunflower)
    print("")
    alice.plants_grow()
    print("")
    alice.report()
    print("")
    print(alice.info())
    alice.plant_type(alice)
    print("")
    print(f"Height validation test: {alice.height_test()}")
    print(
        f"Garden scores - "
        f"{alice.get_owner()}: {alice.get_garden_score()},"
        f" {bob.get_owner()}: {bob.get_garden_score()}"
        )
    print(GardenManager.get_total_gardens())


if __name__ == "__main__":
    main()
