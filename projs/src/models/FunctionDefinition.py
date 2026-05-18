from pydantic import BaseModel
from typing import Dict


class TypeProperty(BaseModel):
    type: str


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Dict[str, TypeProperty]
    returns: TypeProperty
