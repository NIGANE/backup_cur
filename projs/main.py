from json import load
from llm_sdk import Small_LLM_Model
from typing import List, Dict
from torch import torch, Tensor

import sys





vocab: Dict[str, int] = {}
strings: List[str] = []



class Tokenization:
    def __init__(self, model: Small_LLM_Model):
        self.model = model
        self.int_vocab = {}
        self.str_vocab = {}
        self.space_token_id: int = 220
        self.new_line_token_id: int = 198
        self.priority: Dict[str, int] = {}
        self.encoding: List[str] = []
        self.token_ids: List[int] = []
        self.get_vocab()
        self.get_merges()


    def get_merges(self):
        file_path: str = self.model.get_path_to_merges_file()
        try:
            with open(file_path, "r") as f:
                data = f.readlines()
                self.priority = self.load_priority(data)
        except BaseException as e:
            print("err", e)
    def get_vocab(self):
        try:
            file_path: str = self.model.get_path_to_vocab_file()
            with open(file_path, "r") as f:
                data = load(f)
                self.str_vocab = data
                self.int_vocab = {v: k for k, v in self.str_vocab.items()}
        except BaseException:
            print("ERROR: while on get_vocab method")
    
    def encode(self, prompt: str):
        space: str = self.int_vocab[self.space_token_id]
        new_line: str = self.int_vocab[self.new_line_token_id]
        self.encoding = [char for char in prompt.replace(" ",space).replace("\n", new_line)]
        i = 0
        while True:
            if not self.merge(self.get_next_max_prio()):
                break
        for ele in self.encoding:
            self.token_ids.append(self.str_vocab[ele])
        return torch.tensor([self.token_ids])
    
    def decode(self, token_ids: List[int] | Tensor):
        tt: List[int] = token_ids[0].tolist() if type(token_ids) == Tensor else token_ids
        re: str = ""
        for ele in tt:
            re += self.int_vocab[ele].replace(self.int_vocab[self.space_token_id], " ")

        return [re] if type(token_ids) == Tensor else re
        
    def load_priority(self, lines: List[str]):
        rank = 0
        re: Dict[str, int] = {}
        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                continue
            if line is None:
                continue
            duo = tuple(ele for ele in line.split())
            re[duo] = rank
            rank += 1
        return re
    
    def get_next_max_prio(self):
        i = 0
        max_prio = float('+inf')
        while i < len(self.encoding) - 1:
            j = i + 1
            pair = tuple([self.encoding[i], self.encoding[j]])
            if (pair in self.priority and self.priority.get(pair) < max_prio):
                max_prio = self.priority.get(pair)
            i += 1
        return max_prio

    def merge(self, max_prio: int):
        new: List[str] = []
        merged: int = 0

        i = 0
        while i < len(self.encoding) - 1:
            if (self.priority.get(tuple([self.encoding[i], self.encoding[i + 1]])) == max_prio):
                new.append(self.encoding[i] + self.encoding[i + 1])
                merged = 1
                i += 2
                continue
            new.append(self.encoding[i])
            i += 1
        if i == len(self.encoding) - 1:
            new.append(self.encoding[i])
        self.encoding = new
        return True if merged else False
        

tty = Tokenization(Small_LLM_Model())
pt = "What is the sum of 2 and 3?"
static = tty.encode(pt)
dynamic = tty.model.encode(pt)
print("static: ", static)
print("dynamic: ", dynamic)
# print(encode)
# print(decode)
# print(my_decode)

# prompt = "philosofre world"
# char = vocab_int_str[model.encode(" ")[0].tolist()[0]]
# ready = prompt.replace(" ", " " + char).split(" ")

# token_ids = []
# for ele in ready:
#     i = len(ele)
#     sub = ele
#     while True:
#         if sub[:i] in strings:
#             token_ids.append(vocab[sub[:i]])
#             if i == len(ele):
#                 break
#             else:
#                 sub = sub[i:]
#         else:
#             i -= 1
#         if i == 0:
#             break

# print(f"original: {[model.decode(ele) for ele in model.encode(prompt).tolist()[0]]}")        
# print(f"compromized: {[model.decode(ele) for ele in token_ids]}")



def generate(model: Small_LLM_Model, prompt: str) -> str:
    tokens_id = model.encode(prompt)[0].tolist()
    logits = model.get_logits_from_input_ids(tokens_id)
    print("logits: ", logits)
    max_tokens = torch.argmax(torch.tensor(logits))

    # print(f"{max_tokens.tolist()} : {vocab_int_sr[max_tokens.tolist()]}")
    return model.decode(max_tokens)

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