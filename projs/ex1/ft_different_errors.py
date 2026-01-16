def garden_operations(err_type: str) -> int:
    """
    Triggers specific Python exceptions based
        on the provided error type string.

    This function is designed for demonstration purposes to show how different
        runtime errors are handled in Python.

    Args:
        err_type (str): The type of error to trigger. Options are:
            "value", "zero", "file", or "key".

    Returns:
        int: This function is intended to fail before returning a value,
            though it is typed to return an int.

    Raises:
        ValueError: Occurs if err_type is "value" (string to int conversion).
        ZeroDivisionError: Occurs if err_type is "zero" (division by zero).
        FileNotFoundError: Occurs if err_type is "file" (missing file access).
        KeyError: Occurs if err_type is "key"
        (accessing a missing dictionary key).
    """
    if err_type == "value":
        return int("abc")
    elif err_type == "zero":
        return 4 / 0
    elif err_type == "file":
        return open("missing.txt")
    elif err_type == "key":
        d: dict[str, str] = {"name": "achraf"}
        return d['missing_plant']


def test_error_types() -> None:
    """
    Executes a series of tests to demonstrate
        exception handling for garden operations.

    Each operation is wrapped in a try-except-finally block to ensure that
        the program flow continues even after an error is encountered.
    """
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    finally:
        print("")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    finally:
        print("")
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'")
    finally:
        print("")
    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    finally:
        print("")
    print("Testing multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("zero")
    except (ValueError, ZeroDivisionError):
        pass
    print("Caught an error, but program continues!")
    print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
