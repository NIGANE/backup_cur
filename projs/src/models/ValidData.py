from typing import List, Dict, Any, Optional
from src.models.PromptValidation import PromptValidation


class ValidData():
    def __init__(
            self, functions_definitions: List[Dict[str, Any]],
            input_prompts: List[PromptValidation], out: str,
            model: Optional[str]) -> None:
        self.funcs = functions_definitions
        self.prompts = input_prompts
        self.output_file = out
        self.model = model


class InvalidData():
    def __init__(self) -> None:
        return None
