class Plant:
    count = 0
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.ag = age
        Plant.count += 1
        print(f"Created: {self.name} ({self.height}cm, {self.ag} days)")


def ft_plant_factory(data: list) -> list:
    re = []
    for plant in data:
        re.append(Plant(plant["name"], plant["height"], plant["age"]))
    return re
    # return [Plant(item["name"], item["height"], item["age"]) for item in data]


def main() -> None:
    data = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120},
        ]
    plants = ft_plant_factory(data)
    print(f"Total plants created: {Plant.count}")

if __name__ == "__main__":
    main()
