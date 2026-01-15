
class TestClass:
    def __new__(cls):
        return "hello"

    def __init__(s):
        print("ins new class")


def main():
    print(type(TestClass))
    new = TestClass()
    print(new)


if __name__ == "__main__":
    main()