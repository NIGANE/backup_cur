from enum import Enum

class Test(Enum):
    A = 'a'
    B = 'b'

print(Test.A)
print(Test.A.name)
print(Test.A.value)