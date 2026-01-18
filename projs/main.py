class Me:

    def __init__(self, name):
        self.name = name
        self.age = ""
    pass


addOne = Me("achraf")
print(addOne.name)
print(addOne.age)
addOne.age = 45
print(addOne.age)