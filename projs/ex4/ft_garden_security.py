class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        print(f"Plant created: {self.name}")

    def set_height(self, height: float):
        if (height > 0 and height > self.height):
            self.height = height
            print(f"Height updated {self.height}cm [OK]")
        else :
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
    def set_age(self, age: int):
        if (age > 0 and age > self.age):
            self.age = age
            print(f"Age updated {self.age} days [OK]")
        else :
            print("Age value is not valid")
    def get_height(self):
        return self.height
    def get_age(self):
        return self.age
    

def get_info(plant: type[SecurePlant]):
    print(f"Current plant: {plant.__name__} (25cm, 30 days)")
