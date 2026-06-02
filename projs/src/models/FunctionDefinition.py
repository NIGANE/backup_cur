from pydantic import BaseModel
from enum import Enum
from typing import Dict, Optional


class ValidTypes(Enum):
    STRING = "string"
    NUMBER = "number"
    BOOL = "boolean"
    INT = "integer"
    NONE = "None"


class TypeProperty(BaseModel):
    type: ValidTypes = (ValidTypes.STRING.value
                        or ValidTypes.NUMBER.value or ValidTypes.BOOL.value
                        or ValidTypes.INT.value or ValidTypes.NONE.value)


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Optional[Dict[str, TypeProperty]] = None
    returns: TypeProperty
