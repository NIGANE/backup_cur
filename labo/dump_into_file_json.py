from enum import Enum
class ValidTypes(Enum):
    STRING = "string"
    NUMBER = "number"
    BOOL = "boolean"
    INT = "integer"
    NONE = "None"


print(ValidTypes.STRING.name)




