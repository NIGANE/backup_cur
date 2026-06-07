from pydantic import BaseModel
from enum import Enum
from typing import Dict, Optional


class ValidTypes(Enum):
    STRING = "string"
    NUMBER = "number"
    BOOL = "boolean"
    NONE = "None"


class TypeProperty(BaseModel):
    type: ValidTypes


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Optional[Dict[str, TypeProperty]] = None
    returns: TypeProperty
