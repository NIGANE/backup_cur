from pydantic import BaseModel, model_validator, ConfigDict


class PromptValidation(BaseModel):
    """Validate and normalize a prompt.

    This model ensures that the input prompt adheres to the expected schema
    and performs basic normalization before it is used by the constrained
    decoding pipeline.

    Attributes:
        prompt: The prompt text to validate and normalize.
    """
    model_config = ConfigDict(extra="forbid")
    prompt: str

    @model_validator(mode="after")
    def preparing_prompt(self) -> 'PromptValidation':
        """Normalize the prompt after validation.

        Leading and trailing whitespace is removed to ensure the prompt is in
        a consistent format before further processing.

        Returns:
            The validated and normalized prompt model.
        """
        self.prompt = self.prompt.strip()
        return self
