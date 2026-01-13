class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self, cm):
        self.height += cm
    def age(self, d):
        self.age += d
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"
    

def main():
    print("=== Day 1 ===")
    rosee = Plant("rose", 25, 30)
    print(rosee.get_info())
    rosee.grow()


if __name__ == "__main__":
    main()
