class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for errors related to plants in the garden."""
    # def __init__(self, message="issue with the plant."):
    #     super().__init__(f"{message}")
    pass


class WaterError(GardenError):
    """Exception raised for errors related to watering plants."""
    pass


def ft_custom_errors() -> None:
    """Function to demonstrate custom error handling in a garden context."""
    plant = {"name": "tomato", "status": "wilting"}
    water_level = 0

    print("=== Custom Garden Errors Demo ===")
    print("")
    print("Testing PlantError...")
    try:
        if (plant["status"] == "wilting"):
            raise PlantError(
                f"The {plant['name']} plant is wilting!"
                )
    except (PlantError) as pe:
        print("Caught PlantError: " + str(pe))

    print("")
    print("Testing WaterError...")
    try:
        if water_level < 1:
            raise WaterError("Not enough water in the tank!")
    except WaterError as we:
        print("Caught WaterError: " + str(we))

    print("")
    print("Testing catching all garden errors...")

    try:
        if (plant["status"] == "wilting"):
            raise PlantError(
                f"The {plant['name']} plant is wilting!"
                )
    except GardenError as ge:
        print("Caught a GardenError: " + str(ge))
    try:
        if water_level < 1:
            raise WaterError("Not enough water in the tank!")
    except GardenError as er:
        print("Caught a GardenError: " + str(er))
    print("")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
