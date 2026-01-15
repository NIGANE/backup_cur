class GardenManager:

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        self.count = 0
        self.total_growth = 0
    
    def info(self):
        return f"Plant added: {self.count}, Total growth: {self.total_growth}cm"
    def report(self):
        print(f"=== {self.owner.capitalize()}'s Garden Report ===")
        print("Plants in the garden:")
        for plant in self.plants:
            print(plant.describe())

    def add_plant(self, *plants: type['Plant']):
        for plant in plants:
            self.plants.append(plant)
            self.count += 1
            print(f"Added {plant.name} to {self.owner.capitalize()}'s garden")

    def plants_grow(self):
        print(f"{self.owner.capitalize()} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
    @staticmethod
    def title():
        return ("=== Welcome to the Garden Manager ===\n")

    @classmethod
    def plant_type(cls, owner: type['GardenManager']) -> None:
        data = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
        for plant in owner.plants:
            if isinstance(plant, PrizeFlower):
                data["PrizeFlower"] += 1
            elif isinstance(plant, FloweringPlant):
                data["FloweringPlant"] += 1
            else:
                data["Plant"] += 1
        print(
            f"Plant types: {data["Plant"]} regular,"
            f" {data["FloweringPlant"]} flowering,"
            f" {data["PrizeFlower"]} prize-winning"
        )
    


class Plant():

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self, height: int = 1):
        self.height += height
        print(f"{self.name.capitalize()} grew {height}cm")
    
    def describe(self):
        return f"- {self.name.capitalize()}: {self.height}cm"
  

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int , color: str):
        super().__init__(name, height)
        self.color = color

    def describe(self):
        return super().describe() + f", {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def describe(self):
        return super().describe() + f", Prize points: {self.points}"



def main():
    print(GardenManager.title())
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "Red")
    sunflower = PrizeFlower("Sunflower", 50, "Yellow", 10)
    alice = GardenManager("alice")
    alice.add_plant(oak, rose, sunflower)
    print("")
    alice.plants_grow()
    print("")
    alice.report()
    print("")
    print(alice.info())
    alice.plant_type(alice)
    


if __name__ == "__main__":
    main()

