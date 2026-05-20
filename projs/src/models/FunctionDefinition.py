from pydantic import BaseModel
from typing import Dict, Optional


class TypeProperty(BaseModel):
    type: str = "string" or "number" or "boolean" or "integer" or "None" or "array"


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Optional[Dict[str, TypeProperty]] = None
    returns: TypeProperty
