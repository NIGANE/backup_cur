def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> None:
    """
    Validates the environmental conditions for a specific plant.

    This function checks if the provided water and sunlight metrics fall within
        acceptable biological ranges. If any value is outside these bounds, it
        raises and catches a ValueError to notify the user.

    Args:
        plant_name (str): The name of the plant being checked.
        water_level (int): The current water level (Scale: 1-10).
        sunlight_hours (int): Total hours of sunlight received (Range: 2-12).

    Raises:
        ValueError: If plant_name is None, water_level is outside [1, 10],
            or sunlight_hours is outside [2, 12].

    Note:
        The function handles its own exceptions internally, printing the
            error message to the console.
    """
    try:
        if (plant_name is None):
            raise ValueError("Plant name cannot be empty!")
        if (water_level > 10):
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if (water_level < 1):
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if (sunlight_hours > 12):
            err = f"Sunlight hours {sunlight_hours} is too high (max 12)"
            raise ValueError(err)
        if (sunlight_hours < 2):
            err = f"Sunlight hours {sunlight_hours} is too low (min 2)"
            raise ValueError(err)
    except ValueError as err:
        print(f"Error: {err}")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Runs automated tests against check_plant_health to verify boundary
        validation and error message formatting.
    """
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 2, 2)
    print("")
    print("Testing empty plant name...")
    check_plant_health(None, 2, 2)
    print("")
    print("Testing empty plant name...")
    check_plant_health("tomato", 15, 2)
    print("")
    print("Testing empty plant name...")
    check_plant_health("tomato", 2, 0)
    print("")
    print("All error raising tests completed!")


if (__name__ == "__main__"):
    test_plant_checks()
