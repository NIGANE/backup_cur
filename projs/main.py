class Te:
    def __init__(self):
        self.key: int = 3
    def setings(self):
        self.value = 1

ins: Te = Te()

print(ins.__dict__)
if 'value' not in ins.__dict__:
    print("no attribute setted yet")