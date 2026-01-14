class SecurePlant:

    def __init__(self, name: str, height: int = 0, age: int = 0):
        self.__name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.__name}")

    def set_height(self, height: float):
        if (height > 0):
            self.__height = height
            print(f"Height updated {self.__height}cm [OK]")
        else :
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int):
        if (age > 0):
            self.__age = age
            print(f"Age updated {self.__age} days [OK]")
        else :
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
    
    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age
    def get_info(self):
        return (f"Current plant: {self.__name} ({self.get_height()}cm, {self.get_age()} days)")

def main():
    print("=== Garden Security System ===")
    new_plant = SecurePlant("Rose")
    new_plant.set_height(25)
    new_plant.set_age(30)
    print("")
    new_plant.set_height(-5)
    print("")
    print(new_plant.get_info())



if __name__ == "__main__":
    main()