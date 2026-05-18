from pydantic import BaseModel


class PromptValidation(BaseModel):
    prompt: str
