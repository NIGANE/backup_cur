from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Dict, Optional


class ValidTypes(Enum):
    """Enumerate the primitive types supported by function schemas.

    These values define the set of valid data types that can be used for
    function parameters and return values when constructing schemas for
    constrained decoding.
    """
    STRING = "string"
    NUMBER = "number"
    BOOL = "boolean"
    NONE = "None"
    INTEGER = "integer"


class TypeProperty(BaseModel):
    """Represent the type of a function parameter or return value.

    This model is used as the building block for function signatures,
    ensuring that only supported primitive types are specified.

    Attributes:
        type: The primitive type associated with the parameter or return value.
    """
    model_config = ConfigDict(extra="forbid")
    type: ValidTypes


class FunctionDefinition(BaseModel):
    """Represent the schema of a callable function.

    This model defines the metadata required to describe a function for
    constrained decoding, including its name, description, parameters, and
    return type.

    Attributes:
        name: The name of the function.
        description: A brief description of the function's purpose.
        parameters: A mapping of parameter names to their corresponding type
            definitions. Defaults to ``None`` if the function takes no
            parameters.
        returns: The type of the value returned by the function.
    """
    model_config = ConfigDict(extra="forbid")
    name: str
    description: str
    parameters: Optional[Dict[str, TypeProperty]] = None
    returns: TypeProperty
