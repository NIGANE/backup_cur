#!/usr/bin/python3
class SecurePlant:
    """
        Represents a plant with restricted access to its internal state.

        Attributes
        ----------
        __name : str
            Name of the plant.
        __height : int
            Height of the plant in centimeters.
        __age : int
            Age of the plant in days.
    """

    def __init__(self, name: str, height: int = 0, age: int = 0):
        """
        Initialize a SecurePlant instance.

        Parameters
        ----------
        name : str
            Name of the plant.
        height : int, optional
            Initial height of the plant in centimeters.
        age : int, optional
            Initial age of the plant in days.
        """
        self.__name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.__name}")

    def set_height(self, height: int):
        """
        Update the height of the plant if the value is valid.

        Parameters
        ----------
        height : int
            New height of the plant in centimeters.
        """
        if (height > 0):
            self.__height = height
            print(f"Height updated {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int):
        """
        Update the age of the plant if the value is valid.

        Parameters
        ----------
        age : int
            New age of the plant in days.
        """
        if (age > 0):
            self.__age = age
            print(f"Age updated {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        """
        Return the current height of the plant.

        Returns
        -------
        int
            Height of the plant in centimeters.
        """
        return self.__height

    def get_age(self):
        """
        Return the current age of the plant.

        Returns
        -------
        int
            Age of the plant in days.
        """
        return self.__age

    def get_info(self):
        """
        Return a formatted description of the plant.

        Returns
        -------
        str
            A string containing the plant name, height, and age.
        """
        return (
            f"Current plant: {self.__name} "
            f"({self.get_height()}cm, {self.get_age()} days)"
         )


def main() -> None:
    """
    Demonstrate secure creation and modification of a plant instance.
    """
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
