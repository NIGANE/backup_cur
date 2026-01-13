class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self,):
        self.height += 0.81
    def age(self):
        self.age += 1
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"
    

def main():
    print("=== Day 1 ===")
    rosee = Plant("rose", 25, 30)
    print(rosee.get_info())
    i = 1
    while (i < 7):
        rosee.grow()
        rosee.age()
        i += 1
    print("=== Day 7 ===")
    print(rosee.get_info())
    print(f"Growth this week: {i * 0.81}cm")


if __name__ == "__main__":
    main()
