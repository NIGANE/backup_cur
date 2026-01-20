def check_temperature(temp_str: str) -> int:
    """
    Validates and checks if a temperature string is within the safe range

    The function attempts to convert the input string to an integer and checks
        it against a safe threshold (0°C to 40°C).

    Args:
        temp_str (str): The temperature value as a string (e.g., "25").

    Returns:
        int: The parsed temperature if successful, or -1 if a ValueError
            occurred or the input was invalid.

    Note:
        Success or failure
            messages are printed directly to the standard output.
    """
    tp = -1
    try:
        tp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        if (tp > 40):
            print(f"Error: {tp}°C is too hot for plants (max 40°C)")
        elif (tp < 0):
            print(f"Error: {tp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {tp}°C is perfect for plants!")
    return tp


def test_temperature_input() -> None:
    """
    Runs a suite of test cases for the check_temperature function.

    Tests include a valid temperature, a non-numeric string, and values
    exceeding the high and low safety boundaries.
    """
    print("=== Garden Temperature Checker ===")
    print("")
    print("Testing temperature: 25")
    check_temperature("25")
    print("")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("")
    print("Testing temperature: 100")
    check_temperature("100")
    print("")
    print("Testing temperature: -50")
    check_temperature("-50")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
