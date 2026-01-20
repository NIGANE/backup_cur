
class WaterError(Exception):
    """
    Exception raised for errors in the plant watering process.

    Attributes:
        message -- explanation of why the watering failed
    """
    pass


def water_plants(plant_list: list[str]) -> None:
    """
    Iterates through a list of plants and performs the watering process.

    Args:
        plant_list (list[str]): A list of plant names to be watered.

    Raises:
        WaterError: If a `None` value is encountered in the plant list.

    Note:
        The 'finally' block ensures that the watering system is shut down
        regardless of whether the operation succeeded or failed.
    """
    print("Opening watering system")
    err = 0
    try:
        for plant in plant_list:
            if (plant is None):
                raise WaterError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except WaterError as we:
        print(f"Error: {we}")
        err = 1
    finally:
        print("Closing watering system (cleanup)")
    if (not err):
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Tests the watering system with both valid and invalid plant lists to
    demonstrate custom exception handling and system cleanup.
    """
    print("=== Garden Watering System ===")
    print("")

    print("Testing normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)

    print("")

    print("Testing with error...")
    bad_plants = ["tomato", None]
    water_plants(bad_plants)

    print("")
    print("Cleanup always happens, even with errors!")


if (__name__ == "__main__"):
    test_watering_system()
