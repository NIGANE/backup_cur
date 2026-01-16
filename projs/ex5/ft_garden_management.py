class GardenManager:

    def __init__(s, wl: int = 0) -> None:
        s.__plants = []
        s.__water_level = wl

    def add_plants(s, plants: list[str]) -> None:
        try:
            for p in plants:
                if (p["name"] is None):
                    raise ValueError("Plant name cannot be empty!")
                s.__plants.append(p)
                print(f"Added {p["name"]} successfully")
        except ValueError as er:
            print(f"Error adding plant: {er}")

    def water_plants(s) -> None:
        print("Opening watering system")
        try:
            for p in s.__plants:
                p["water_level"] += 1
                print(f"Watering {p["name"]} - success")
        finally:
            print("Closing watering system (cleanup)")

    def health_check(s) -> None:
        print("Checking plant health...")
        try:
            for pl in s.__plants:
                if (pl["water_level"] > 10):
                    err_obj = {
                        "name": pl["name"],
                        "message": (f"Water level {pl["water_level"]} "
                                    f"is too high (max 10)")
                                }
                    raise ValueError(err_obj)
                if (pl["water_level"] < 1):
                    err_obj = {
                        "name": pl["name"],
                        "message": (f"Water level {pl["water_level"]} "
                                    f"is too low (min 1)")
                                }
                    raise ValueError(err_obj)
                if (pl["sunlight_hours"] > 12):
                    err_obj = {
                        "name": pl["name"],
                        "message": f"Sunlight hours {pl["sunlight_hours"]} "
                        f"is too high (max 12)"
                    }
                    raise ValueError(err_obj)
                if (pl["sunlight_hours"] < 2):
                    err_obj = {
                        "name": pl["name"],
                        "message": f"Sunlight hours {pl["sunlight_hours"]} "
                        f"is too low (min 2)"
                    }
                    raise ValueError(err_obj)
                print(
                    f"{pl["name"]}: healthy (water: {pl["water_level"]}"
                    f", sun: {pl["sunlight_hours"]})"
                    )
        except ValueError as e:
            print(
                f"Error checking {e.args[0]["name"]}: "
                f"{e.args[0]["message"]}"
                )

    def tank_check(s) -> None:
        try:
            if (s.__water_level < 1):
                err = "Not enough water in tank"
                raise ValueError(err)
        except ValueError as er:
            print(f"Caught GardenError: {er}")
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    gardens = [
        {"name": "tomato", "water_level": 4, "sunlight_hours": 8},
        {"name": "lettuce", "water_level": 14, "sunlight_hours": 8},
        {"name": None, "water_level": 15, "sunlight_hours": 8},
        ]

    garden = GardenManager()
    print("Adding plants to garden...")
    garden.add_plants(gardens)
    print("")
    garden.water_plants()
    print("")
    garden.health_check()
    print("")
    print("Testing error recovery...")
    garden.tank_check()
    print("")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
