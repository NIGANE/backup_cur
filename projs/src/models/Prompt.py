from typing import Dict, Any


class Prompt():
    """Represent a prompt and its associated metadata.

    This class encapsulates the prompt text along with optional metadata,
    including a name and a collection of parameters. It serves as the base
    representation of a prompt used throughout the constrained decoding
    pipeline.

    Attributes:
        prompt: The prompt text provided to the language model.
        name: The name associated with the prompt. Defaults to an empty string.
        parameters: A mapping of parameter names to their corresponding values.
    """
    def __init__(self, prompt: str):
        """Initialize a prompt instance.

        Args:
            prompt: The prompt text to be processed by the language model.
        """
        self.prompt: str = prompt
        self.name: str = ""
        self.parameters: Dict[str, Any] = {}
