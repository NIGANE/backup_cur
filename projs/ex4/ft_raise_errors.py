def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> None:
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
