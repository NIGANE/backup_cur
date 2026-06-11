from llm_sdk import Small_LLM_Model
from torch import torch, Tensor, argmax, tensor, full
from typing import  List, Any, Dict
from src.models.FunctionDefinition import ValidTypes
from src.tools.tools import in_string
from functools import reduce
from json import load
from src.models.ErrorHandler import MyError


class Tokenization:
    def __init__(self, model: Small_LLM_Model):
        self.model = model
        self.int_vocab = {}
        self.str_vocab = {}
        self.space_token_id: int = 220
        self.get_vocab()

    def get_vocab(self):
        try:
            file_path: str = self.model.get_path_to_vocab_file()
            with open(file_path, "r") as f:
                data = load(f)
                self.str_vocab = data
                self.int_vocab = {v: k for k, v in self.str_vocab.items()}
        except BaseException:
            raise print("ERROR: while on get_vocab method")
    
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
        tt: List[int] = token_ids.tolist() if type(token_ids) == Tensor else token_ids
        re: str = ""
        for ele in tt:
            re += self.int_vocab[ele].replace(self.int_vocab[self.space_token_id], " ")

        return [re] if type(token_ids) == Tensor else re
        


class Prompt():
    def __init__(self, prompt: str):
        self.prompt: str = prompt
        self.name: str = ""
        self.parameters: Dict[str, Any] = {}


class Agent():
    def __init__(
            self, model: Small_LLM_Model, prompts: List[str],
            functions_definitions: List[Dict]):
        self.fns = functions_definitions
        self.fn_names = [fn['name'] for fn in self.fns]
        self.model = model
        self.constrained_prompt = ""
        self.max_tokens: int = 5
        self.prompts: List[Prompt] = []
        self.tokenizer = Tokenization(model)
        for prompt in prompts:
            self.prompt = Prompt(prompt)
            print(f"resolving prompt: {self.prompt.prompt}")
            self.generate_json_valid()
            self.prompts.append(self.prompt)
            self.empty()
            # print()
            # print({"name": self.prompt.name, "params": self.prompt.parameters})
            # break

    def empty(self):
        self.constrained_prompt = ""

    def generate_json_valid(self):
        # constrained decoding the function name
        self.generate_function_name()
        selected_fn = []
        if (self.prompt.name not in self.fn_names):
            self.prompt.name = "undefined"
            return
        else:
            selected_fn = [
                fn for fn in self.fns if fn['name'] == self.prompt.name][0]

        # generating the params
        if selected_fn['parameters'] is not None:
            self.generate_params()

    def build_prompt(self) -> str:
        header = "starting point, avalaible functions:\n"
        preparing_list: List[str] = []
        item = ""
        for fn in self.fns:
            item += "- " + fn.get("name") + "("
            params = list(fn.get("parameters").keys())
            for i in range(len(params)):
                item += f"{params[i]}: "
                item += f"{fn.get("parameters")[params[i]].value}"
                if i != len(params) - 1:
                    item += ", "
            item += ")\n"
            preparing_list.append(item)
            item = ""
        return reduce(lambda a, b: a + b, preparing_list, header)

    def generate_function_name(self):
        authorized_ids = [
            self.tokenizer.encode(fn_name).tolist()[0]
            for fn_name in self.fn_names
            ]
        self.constrained_prompt = self.build_prompt()
        self.constrained_prompt += (
            f"the best function to traite "
            f"this user request: '{self.prompt.prompt}' is :")

        i = 0
        while (i < self.max_tokenized(authorized_ids)):
            res = self.prompting_by_token(
                self.constrained_prompt, [ele[i] for ele in authorized_ids])
            self.prompt.name += res
            self.constrained_prompt += res
            authorized_ids = self.filter_authorized_ids(self.prompt.name)
            i += 1

    @staticmethod
    def max_tokenized(tokens: List[List[int]]) -> int:
        if len(tokens) == 0:
            return 0
        max_size = len(tokens[0])
        for tok in tokens:
            if len(tok) > max_size:
                max_size = len(tok)
        return max_size

    def filter_authorized_ids(self, pattern: str) -> List[List[int]]:
        return [
            self.tokenizer.encode(fn_name).tolist()[0]
            for fn_name in self.fn_names
            if fn_name.startswith(pattern)
        ]

    def prompting_by_token(self, ppt: str, tokens: List[int]) -> str:
        prompt_ids = self.tokenizer.encode(ppt)[0].tolist()
        logits = self.model.get_logits_from_input_ids(prompt_ids)
        torch_logits: Tensor = tensor(logits)
        mask = full(torch_logits.shape, float('-inf'))
        for ele in tokens:
            mask[ele] = 0.0
        filtered_logits = torch_logits + mask
        next_token_id = [argmax(filtered_logits).tolist()]
        return self.tokenizer.decode(next_token_id)

    def generate_params(self):
        target_func = [
            ele for ele in self.fns if ele["name"] == self.prompt.name][0]
        self.constrained_prompt = f"You are a parameter extraction engine.\n"

        self.constrained_prompt += f"User Prompt: {self.prompt.prompt}\n"
        self.constrained_prompt += f"Function to use: {self.prompt.name}"
        params = list(target_func["parameters"].keys())
        item = "("
        for i in range(len(params)):
            item += f"{params[i]}: "
            ttp = target_func.get("parameters")[params[i]].value
            item += f"{"str" if ttp == "string" else ttp}"
            if i != len(params) - 1:
                item += ", "
        item += ")\n"
        item += "{"
        item += f'"function": "{self.prompt.name}"'

        self.constrained_prompt += item
        self.constrained_prompt += ', "parameters": {'
        prompt = self.constrained_prompt
        # next_word = ""
        # while True:
        #     prompt += next_word
        #     next_word = self.generate(prompt)
        #     print(prompt + next_word)
        #     if "}" in next_word:
        #         break
        # raise MyError("done")
        params: Dict[str, Any] = ([
            fn for fn in self.fns
            if fn['name'] == self.prompt.name][0]['parameters'])
        i = 0
        for key in params:
            self.constrained_prompt += f'"{key}": '
            if (params[key].value == ValidTypes.NUMBER.value):
                self.prompting_number_params(key, params[key].value)
            else:
                self.prompting_str_params(key, params[key].value)
            i += 1
            if (i != len(params)):
                self.constrained_prompt += ", "

    def prompting_str_params(self, key: str, type: str) -> None:
        i = 0
        founded = ""
        self.constrained_prompt += '"'
        while True:
            next_word = self.generate(self.constrained_prompt + founded)
            if '"' in next_word:
                break
            founded += next_word
        self.prompt.parameters[key] = founded
        self.constrained_prompt += str(founded) + '"'

    def prompting_number_params(self, key: str, type: str):
        i: int = 0
        founded: str = ""
        self.constrained_prompt += '" '
        authorized_ids = [
            self.tokenizer.encode(ele)[0].tolist()[0] for ele in [" -", " "]]
        next_word = self.prompting_by_token(
                self.constrained_prompt + founded, authorized_ids)
        founded += next_word
        while i < self.max_tokens:
            next_word = self.prompting_by_token(
                self.constrained_prompt + founded,
                self.tokenizer.encode("0123456789\n")[0].tolist())
            if (next_word == "'\n"):
                break
            if (
                in_string(
                    (founded + next_word.strip()).strip(), self.prompt.prompt)
                    ):
                founded += next_word
            i += 1
        self.constrained_prompt += (founded + '"').strip()
        self.prompt.parameters[key] = float(founded)

    def resolve_prompts(self) -> List[Prompt]:
        return self.prompts

    def generate(self, prompt: str) -> str:
        tokens_id = self.tokenizer.encode(prompt)[0].tolist()
        logits = self.model.get_logits_from_input_ids(tokens_id)
        max_tokens = [argmax(tensor(logits)).tolist()]
        return self.tokenizer.decode(max_tokens)