from pydantic import BaseModel, model_validator


class PromptValidation(BaseModel):
    prompt: str

    @model_validator(mode="after")
    def preparing_prompt(self):
        self.prompt = self.prompt.strip().lower()
        return self
