def garden_operations(err_type: str) -> int:
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
        print(
            f"Caught "
            f"KeyError: {e}"
            )
    finally:
        print("")
    print("Testing multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("zero")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        pass
    print("Caught an error, but program continues!")
    print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
