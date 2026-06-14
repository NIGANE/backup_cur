from typing import List, Dict, Any
from src.models.PromptValidation import PromptValidation


class ValidData():
    def __init__(
            self, functions_definitions: List[Dict[str, Any]],
            input_prompts: List[PromptValidation], out: str) -> None:
        self.funcs = functions_definitions
        self.prompts = input_prompts
        self.output_file = out


class InvalidData():
    def __init__(self) -> None:
        return None
