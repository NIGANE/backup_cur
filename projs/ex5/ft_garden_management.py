
class GardenError(Exception):
    """
    Custom exception for garden-specific logic and hardware failures.
    Inherits standard argument handling automatically from Exception.
    Used to categorize errors distinct from standard Python exceptions.
    Provides a clean way to filter garden-related issues in try blocks.
    """
    pass


class PlantError(GardenError):
    """Exception raised for errors related to plants in the garden."""
    pass


class WaterError(GardenError):
    """Exception raised for errors related to watering plants."""
    pass


class GardenManager:
    """
    Manages a collection of plants and oversees watering and health validation.

    This class acts as the central controller for garden operations,
        maintaining internal state for plant data and system resources
        like water levels.

    Attributes:
        wl (int): Initial water level for the garden tank.
    """

    def __init__(s, wl: int = 0) -> None:
        """
        Initializes the GardenManager with an empty plant list
            and a tank level.
        """
        s.__plants = []
        s.__water_level = wl

    def add_plants(s, plants: list[str]) -> None:
        """
        Adds a list of plant dictionaries to the internal registry.

        Args:
            plants (list[dict]): A list of dictionaries, where each dict
                must contain a 'name' key.

        Raises:
            PlantError: If a plant in the list has a 'None'
                value for its name.
        """
        try:
            for p in plants:
                if (p["name"] is None):
                    raise PlantError("Plant name cannot be empty!")
                s.__plants.append(p)
                print(f"Added {p['name']} successfully")
        except PlantError as er:
            print(f"Error adding plant: {er}")

    def water_plants(s) -> None:
        """
        Increments the water level of all registered plants.

        Note:
            Utilizes a 'finally' block to ensure the watering system hardware
            (simulated) is always shut down safely.
        """
        print("Opening watering system")
        try:
            for p in s.__plants:
                p["water_level"] += 1
                print(f"Watering {p['name']} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(s) -> None:
        """
        Evaluates the health status of all plants based on water
            and light levels.

        If a plant exceeds safe thresholds, a GardenError containing a
            dictionary of error details is raised and handled.
        """
        print("Checking plant health...")
        try:
            for pl in s.__plants:
                if (pl["water_level"] > 10):
                    err_obj = {
                        "name": pl["name"],
                        "message": (f"Water level {pl['water_level']} "
                                    f"is too high (max 10)")
                                }
                    raise WaterError(err_obj)
                if (pl["water_level"] < 1):
                    err_obj = {
                        "name": pl["name"],
                        "message": (f"Water level {pl['water_level']} "
                                    f"is too low (min 1)")
                                }
                    raise WaterError(err_obj)
                if (pl["sunlight_hours"] > 12):
                    err_obj = {
                        "name": pl["name"],
                        "message": f"Sunlight hours {pl['sunlight_hours']} "
                        f"is too high (max 12)"
                    }
                    raise PlantError(err_obj)
                if (pl["sunlight_hours"] < 2):
                    err_obj = {
                        "name": pl["name"],
                        "message": f"Sunlight hours {pl['sunlight_hours']} "
                        f"is too low (min 2)"
                    }
                    raise PlantError(err_obj)
                print(
                    f"{pl['name']}: healthy (water: {pl['water_level']}"
                    f", sun: {pl['sunlight_hours']})"
                    )
        except GardenError as e:
            print(
                f"Error checking {e.args[0]['name']}: "
                f"{e.args[0]['message']}"
                )

    def tank_check(s) -> None:
        """
        Checks the system's main water reservoir level.

        Prints an error message if the tank is empty but ensures system
            recovery through the use of a 'finally' block.
        """
        try:
            if (s.__water_level < 1):
                err = "Not enough water in tank"
                raise WaterError(err)
        except GardenError as er:
            print(f"Caught GardenError: {er}")
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    """
    Simulates garden operations to test plant additions and health checks.
    It verifies that the system handles invalid data and low water levels.
    The test ensures that cleanup always occurs via try-finally blocks.
    Final output confirms system stability and successful error recovery.
    """
    gardens = [
        {"name": "tomato", "water_level": 4, "sunlight_hours": 8},
        {"name": "lettuce", "water_level": 14, "sunlight_hours": 8},
        {"name": None, "water_level": 15, "sunlight_hours": 8},
        ]
    print("=== Garden Management System ===")
    print("")

    garden = GardenManager()
    print("Adding plants to garden...")
    garden.add_plants(gardens)

    print("")

    garden.water_plants()

    print("")

    garden.check_plant_health()

    print("")
    print("Testing error recovery...")

    garden.tank_check()

    print("")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
