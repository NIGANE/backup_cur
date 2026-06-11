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
        # self.get_vocab()
        self.get_merges()


    def get_merges(self):
        file_path: str = self.model.get_path_to_merges_file()
        try:
            with open(file_path, "r") as f:
                data = f.read()
                
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
        s: List[str] = prompt.replace(" ", " " + space).split(" ")
        token_ids = []
        for ele in s:
            i = len(ele)
            sub = ele
            while True:
                if sub[:i] in self.str_vocab:
                    token_ids.append(self.str_vocab[sub[:i]])
                    if i == len(ele):
                        break
                    else:
                        sub = sub[i:]
                else:
                    i -= 1
                if i == 0:
                    break
        return torch.tensor([token_ids])
    
    def decode(self, token_ids: List[int] | Tensor):
        tt: List[int] = token_ids[0].tolist() if type(token_ids) == Tensor else token_ids
        re: str = ""
        for ele in tt:
            re += self.int_vocab[ele].replace(self.int_vocab[self.space_token_id], " ")

        return [re] if type(token_ids) == Tensor else re
        


        
tty = Tokenization(Small_LLM_Model())
# print(tty)
pt = "hello from Achraf AKA negane"
# my_encode = tty.encode(pt).tolist()[0]
# encode = tty.model.encode(pt).tolist()[0]
# my_decode = tty.decode(my_encode[0])
# decode = tty.model.decode(encode[0])
# # 
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