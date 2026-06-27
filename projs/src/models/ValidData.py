from typing import List, Dict, Any, Optional
from src.models.PromptValidation import PromptValidation


class ValidData():
    """Store validated input data for the constrained decoding pipeline.

    This class aggregates the validated function definitions, input prompts,
    output destination, and optional model name required to execute the
    pipeline.

    Attributes:
        funcs: The validated function definitions.
        prompts: The validated input prompts.
        output_file: The path to the output file.
        model: The name of the language model to use, if specified.
    """
    def __init__(
            self, functions_definitions: List[Dict[str, Any]],
            input_prompts: List[PromptValidation], out: str,
            model: Optional[str]) -> None:
        """Initialize a validated data container.

        Args:
            functions_definitions: The validated function definitions.
            input_prompts: The validated input prompts.
            out: The path to the output file.
            model: The name of the language model to use, or ``None`` to use
                the default model.
        """
        self.funcs = functions_definitions
        self.prompts = input_prompts
        self.output_file = out
        self.model = model


class InvalidData():
    """Represent an invalid validation result.

    This class acts as a sentinel value indicating that the input validation
    process failed.
    """
    def __init__(self) -> None:
        """Initialize an invalid data marker."""
        return None
