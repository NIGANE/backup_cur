from typing import Dict, Any


class Prompt():
    def __init__(self, prompt: str):
        self.prompt: str = prompt
        self.name: str = ""
        self.parameters: Dict[str, Any] = {}
