
def main():
    try:
        raise ValueError({"value": "val", "message": "mess from error handling"})
    except ValueError as e:
        print(e.args[0]['message'])


if __name__ == "__main__":
    main()