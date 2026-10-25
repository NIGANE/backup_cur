
from src.models import StudentSearchResultsAndAnswer
from transformers import pipeline
from src.error import Error
from pathlib import Path
from typing import List
import json
import os

class Agent:
    def __init__(self, model: str = 'Qwen/Qwen3-0.6B'):
        self.gen = pipeline(
                    'text-generation',
                    model=model,
                    device='cpu'
                    )
        self.file = "answering_doc.json"
    def inference(self, contexts: List[str], query: str):
        
        context: str = "\n\n".join([
            f"- chunk: {ch}" for ch in contexts
        ])
        prompt: str = f"""Use the context below to answer the question.

        Context:
        {context}

        Question: {query}
        Answer:"""
        res = self.gen(
            prompt,
            max_new_tokens=50,
            do_sample=False,
            return_full_text=False 
        )
        return (res[0]['generated_text'])

    def save(self, data: StudentSearchResultsAndAnswer, dest: Path) -> Path:
        if (dest.suffix):
            self.file = dest.name
            dest = dest.parent
        try:
            os.makedirs(dest, exist_ok=True)
            with open(dest / self.file, "w") as f:
                json.dump(
                    data.model_dump(),
                    f,
                    indent=2
                    )
        except Exception as e:
            raise Error(f"{e}")
        else:
            return dest / self.file
