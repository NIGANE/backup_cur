class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name.capitalize()} (Flower): {self.height}cm, {self.age} days, {self.color} color")

    def bloom(self):
        return (f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name.capitalize()} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        return (f"{self.name.capitalize()} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name.capitalize()} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")

    def get_info(self):
        return (f"{self.name} is rich in vitamin C")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("")
    rosee = Flower("rose", 25, 30, "red")
    oak = Tree("oak", 500, 1825, 50)
    tomato = Vegetable("tomato", 80, 90, "summer")

    rosee.