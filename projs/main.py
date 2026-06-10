from json import load
from llm_sdk import Small_LLM_Model
from typing import List, Dict
import torch
import sys


model: Small_LLM_Model = Small_LLM_Model()

file_path: str = model.get_path_to_vocab_file()

vocab: Dict[str, int] = {}
strings: List[str] = []

try:
    with open(file_path, "r") as f:
        data = load(f)
        vocab = data
    strings = list(vocab.keys())
except BaseException:
    print("error")
vocab_int_str = {v: k for k, v in vocab.items()}

prompt = "philosofre world"
char = vocab_int_str[model.encode(" ")[0].tolist()[0]]
ready = prompt.replace(" ", " " + char).split(" ")
print(f"striped array: {ready}")
print(f"original: {[model.decode(ele) for ele in model.encode(prompt).tolist()[0]]}")
token_ids = []
for ele in ready:
    i = len(ele)
    sub = ele
    while True:
        if sub[:i] in strings:
            token_ids.append(vocab[sub[:i]])
            if i == len(ele):
                break
            else:
                sub = sub[i:]
        else:
            i -= 1
        if i == 0:
            break
print(f"compromized: {[model.decode(ele) for ele in token_ids]}")
        



# def generate(prompt: str) -> str:
#     tokens_id = model.encode(prompt)[0].tolist()
#     logits = model.get_logits_from_input_ids(tokens_id)
#     max_tokens = torch.argmax(torch.tensor(logits))

#     # print(f"{max_tokens.tolist()} : {vocab_int_sr[max_tokens.tolist()]}")
#     return model.decode(max_tokens)

# prompt = """You are a parameter extraction engine.
# User Prompt: Reverse the string 'hello'
# Function to use: fn_reverse_string(s: str)
# {"function": "fn_reverse_string", "parameters": {"""""

# next_word: str = ""
# import json
# try:
#     while True:
#         prompt += next_word
#         next_word = generate(prompt)
#         print(prompt + next_word)
#         if "}" in next_word:
#             break
#     # with open("out.json", "w") as f:
#     #     json.dump(f, my_json)
# except BaseException as e:
#     print(f"done : {e}")