

def  check_plant_health(plant_name: str, water_level, sunlight_hours) -> None:
    try:
        for plant in plant_list:
            if (plant is None):
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as we:
        print(f"Error: {we}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    goot_plants = ["tomato", "lettuce", "carrots"]
    water_plants(goot_plants)
    print("Watering completed successfully!")
    print("")
    print("Testing with error...")
    bad_plants = ["tomato", None]
    water_plants(bad_plants)
    print("")
    print("Cleanup always happens, even with errors!")


if (__name__ == "__main__"):
    test_watering_system()
