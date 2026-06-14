from pydantic import BaseModel, model_validator, ConfigDict


class PromptValidation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    prompt: str

    @model_validator(mode="after")
    def preparing_prompt(self):
        self.prompt = self.prompt.strip()
        return self
