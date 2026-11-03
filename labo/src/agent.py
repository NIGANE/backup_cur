from src.models import StudentSearchResultsAndAnswer, MinimalSource
from transformers import pipeline, AutoTokenizer
from src.error import Error
from pathlib import Path
from typing import List, Dict, Tuple, Any
import json
from functools import lru_cache
import os


class Agent:
    def __init__(self, model: str = 'Qwen/Qwen3-0.6B'):
        self.gen = pipeline(
                    'text-generation',
                    model=model,
                    device='cpu'
                    )
        self.tokenizer: Any = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
        self.file: str = "answering_doc.json"

    def inference(self, contexts: List[MinimalSource], query: str
                  ) -> Dict[str, str]:

        return self._inference(
            ((e.file_path, e.first_character_index, e.last_character_index) for e in contexts),
            query
            )

    @lru_cache(maxsize=20)
    def _inference(self, contexts: Tuple[Tuple[str, int, int]], query: str) -> Dict[str, str]:
        prompt: str = self.construct_prompt(query, contexts, self.tokenizer)
        res: List[Dict[str, str]] = self.gen(
            prompt,
            max_new_tokens=100,
            do_sample=False,
            return_full_text=False,
        )
        return (res[0])

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

    @staticmethod
    def build_format_context(search_results: Tuple[Tuple[str, int, int]]) -> str:
        output: str = ""

        for nb, min_src in enumerate(search_results, 1):
            with open(min_src[0], 'r') as f:
                data = f.read()
                output += f"--- source {nb} ---\n"
                output += f"File: {min_src[0]}\n"
                output += f"Character Range: {min_src[1]} "
                output += f"-> {min_src[2]}\n"
                output += "Content:\n"
                output += data[
                    min_src[1]:min_src[2]
                    ] + "\n"
        return output

    @staticmethod
    def build_messsages(question: str, formatted_context: str):
        system_instruction = (
            "You are an expert coding and documentation assistant. "
            "Answer the user's question accurately based ONLY on the provided"
            "context sources. "
            "Provide a direct, concise answer in 1 or 2 lines maximum. "
            "Remember: If the answer cannot be deduced from the context,state "
            "clearly that you do not know."
        )

        user_content = (
            f"Context Sources:\n"
            f"{formatted_context}\n\n"
            f"Question: {question}\n\n"
            f"Answer:"
        )

        return [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_content}
        ]

    @staticmethod
    def construct_prompt(question: str, search_result: Tuple[Tuple[str, int, int]], tokenizer: Any) -> str:
        formatted_context = Agent.build_format_context(search_result)
        messages = Agent.build_messsages(question, formatted_context)

        prompt_text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False
        )
        return prompt_text
