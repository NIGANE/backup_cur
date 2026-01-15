class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        print(
            f"{self.name.capitalize()} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
            )

    def bloom(self):
        return (f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(
            f"{self.name.capitalize()} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )

    def produce_shade(self):
        return (f"{self.name.capitalize()} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, hs, nv: str):
        super().__init__(name, height, age)
        self.harvest_season = hs
        self.nutritional_value = nv
        print(
            f"{self.name.capitalize()} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
            )

    def get_info(self):
        return (
            f"{self.name.capitalize()} is rich in "
            f"{self.nutritional_value.capitalize()}"
            )


def main() -> None:
    print("=== Garden Plant Types ===")
    print("")
    flowers = [("rose", 25, 30, "red"), ("lily", 35, 45, "white")]
    trees = [("oak", 500, 1825, 50), ("pine", 300, 2500, 80)]
    vegetables = [
        ("tomato", 80, 90, "summer", "vitami c"),
        ("carrot", 70, 75, "autumn", "vitamin a")
        ]
    for flower in flowers:
        ins = Flower(*flower)
        print(ins.bloom())
    print("")
    for tree in trees:
        ins = Tree(*tree)
        print(ins.produce_shade())
    print("")
    for vegetable in vegetables:
        ins = Vegetable(*vegetable)
        print(ins.get_info())


if __name__ == "__main__":
    main()
