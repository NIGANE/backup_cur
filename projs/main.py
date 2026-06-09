from json import load
from llm_sdk import Small_LLM_Model
from typing import List, Dict

model: Small_LLM_Model = Small_LLM_Model()

file_path: str = model.get_path_to_vocab_file()

vocab: Dict[str, int] = {}
strings: List[str] = []

try:
    with open(file_path, "r") as f:
        data = load(f)
        vocab = data
    strings = list(vocab.keys())
    print(strings)
except BaseException:
    print("error")

