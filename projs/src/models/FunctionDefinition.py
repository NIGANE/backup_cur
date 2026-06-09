from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Dict, Optional


class ValidTypes(Enum):
    STRING = "string"
    NUMBER = "number"
    BOOL = "boolean"
    NONE = "None"


class TypeProperty(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: ValidTypes


class FunctionDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    description: str
    parameters: Optional[Dict[str, TypeProperty]] = None
    returns: TypeProperty
