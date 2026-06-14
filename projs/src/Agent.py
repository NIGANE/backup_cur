from llm_sdk import Small_LLM_Model
from torch import torch, Tensor, argmax, tensor, full
from typing import List, Any, Dict, Tuple, Optional, Union
from src.models.FunctionDefinition import ValidTypes
from functools import reduce
from json import load
from src.models.ErrorHandler import MyError
from functools import lru_cache


class Tokenization:
    def __init__(self, model: Small_LLM_Model):
        self.model = model
        self.int_vocab: Dict[int, str] = {}
        self.str_vocab: Dict[str, int] = {}
        self.space_token_id: int = 220
        self.new_line_token_id: int = 198
        self.priority: Dict[Tuple[str, str], int] = {}
        self.encoding: List[str] = []
        self.token_ids: List[int] = []
        self.get_vocab()
        self.get_merges()

    def get_merges(self) -> None:
        file_path: str = self.model.get_path_to_merges_file()
        try:
            with open(file_path, "r") as f:
                data = f.readlines()
                self.priority = self.load_priority(data)
        except BaseException as e:
            raise MyError(f"Error: {e}")

    def get_vocab(self) -> None:
        try:
            file_path: str = self.model.get_path_to_vocab_file()
            with open(file_path, "r") as f:
                data = load(f)
                self.str_vocab = data
                self.int_vocab = {v: k for k, v in self.str_vocab.items()}
        except BaseException as e:
            raise MyError(f"Error: {e}")

    def encode(self, prompt: str) -> Tensor:
        space: str = self.int_vocab[self.space_token_id]
        new_line: str = self.int_vocab[self.new_line_token_id]
        self.encoding = [
            char for char in prompt.replace(" ", space).replace("\n", new_line)
            ]
        self.token_ids = []
        while True:
            re = self.get_next_max_prio()
            if not self.merge(re if re == float("+inf") else int(re)):
                break
        for ele in self.encoding:
            self.token_ids.append(self.str_vocab[ele])
        self.encoding = []
        return torch.tensor([self.token_ids])

    def decode(self, token_ids: List[int] | Tensor) -> Union[List[str], str]:
        tt: Union[List[int], Tensor] = (
            token_ids[0].tolist() if isinstance(token_ids, Tensor)
            else token_ids)
        re: str = ""
        for ele in tt:
            re += self.int_vocab[ele].replace(
                self.int_vocab[self.space_token_id], " ")

        return [re] if isinstance(token_ids, Tensor) else re

    def load_priority(self, lines: List[str]) -> Dict[Tuple[str, str], int]:
        rank = 0
        re: Dict[Tuple[str, str], int] = {}

        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                continue
            if line is None:
                continue
            duo: Tuple[str, str] = (line.split()[0], line.split()[1])
            re[duo] = rank
            rank += 1
        return re

    def get_next_max_prio(self) -> float:
        i = 0
        max_prio: float = float('+inf')
        while i < len(self.encoding) - 1:
            j = i + 1
            pair: Tuple[str, str] = (self.encoding[i], self.encoding[j])
            if (pair in self.priority and self.priority[pair] < max_prio):
                max_prio = self.priority[pair]
            i += 1
        return (max_prio)

    def merge(self, max_prio: Union[int, float]) -> bool:
        new: List[str] = []
        merged: int = 0
        i = 0
        if max_prio == float("+inf"):
            return False
        while i < len(self.encoding) - 1:
            exists: Optional[int] = self.priority.get(
                (self.encoding[i], self.encoding[i + 1]))
            if (exists
                    and self.priority[(self.encoding[i], self.encoding[i + 1])]
                    == max_prio):
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


class Prompt():
    def __init__(self, prompt: str):
        self.prompt: str = prompt
        self.name: str = ""
        self.parameters: Dict[str, Any] = {}


class Agent():
    def __init__(
            self, model: Small_LLM_Model, prompts: List[str],
            functions_definitions: List[Dict]):
        self.fns: List[Dict[str, Any]] = functions_definitions
        self.fns.append({
            "name": "fn_undefined",
            "description": (
                "choose if no other function is useable to resolve the prompt"
                ),
            "parameters": {}})
        self.fn_names: List[str] = [fn['name'] for fn in self.fns]
        self.model: Small_LLM_Model = model
        self.constrained_prompt: str = ""
        self.max_tokens: int = 5
        self.prompts: List[Prompt] = []
        self.tokenizer: Tokenization = Tokenization(self.model)
        print("|-> start resolving prompts...")
        for prompt in prompts:
            self.prompt: Prompt = fun(prompt.lower())
            print(f"resolving prompt: {self.prompt.prompt}")
            if (not self.prompt.name):
                self.generate_json_valid()
            self.prompts.append(self.prompt)
            self.empty()

    def empty(self) -> None:
        self.constrained_prompt = ""

    def generate_json_valid(self) -> None:
        # constrained decoding the function name
        self.generate_function_name()
        # print(self.prompt.name)
        selected_fn: Dict[str, Any] = {}
        if (self.prompt.name not in self.fn_names
                or self.prompt.name == "undefined"):
            self.prompt.name = "undefined"
            return
        else:
            selected_fn = [
                fn for fn in self.fns if fn['name'] == self.prompt.name][0]

        # generating the params
        if selected_fn['parameters'] is not None:
            self.generate_params()

    def build_prompt(self) -> str:
        header: str = "starting point, avalaible functions:\n"
        preparing_list: List[str] = []
        item: str = ""
        for fn in self.fns:
            item += "- " + fn["name"] + "("
            if (fn.get("parameters")):
                params: List[str] = list(fn["parameters"].keys())
                for i in range(len(params)):
                    item += f"{params[i]}: "
                    item += f"{fn["parameters"][params[i]].value}"
                    if i != len(params) - 1:
                        item += ", "
            item += f"): {fn["description"]}\n"
            preparing_list.append(item)
            item = ""
        return reduce(lambda a, b: a + b, preparing_list, header)

    def generate_function_name(self) -> None:
        authorized_ids: List[List[int]] = [
            self.tokenizer.encode(fn_name).tolist()[0]
            for fn_name in self.fn_names
            ]
        i: int = 0
        self.constrained_prompt = self.build_prompt()
        self.constrained_prompt += (
            f"the best function to traite "
            "this user request: "
            f"'{self.prompt.prompt if self.prompt.prompt else "empty"}' is :")
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
        prompt_ids: List[int] = self.tokenizer.encode(ppt)[0].tolist()
        logits: List[float] = self.model.get_logits_from_input_ids(prompt_ids)
        torch_logits: Tensor = tensor(logits)
        mask: Tensor = full(torch_logits.shape, float('-inf'))
        for ele in tokens:
            mask[ele] = 0.0
        filtered_logits: Tensor = torch_logits + mask
        next_token_id: List[int] = [int(argmax(filtered_logits).item())]
        re: Union[List[str], str] = self.tokenizer.decode(next_token_id)
        return re[0] if isinstance(re, List) else re

    def generate_params(self) -> None:
        target_func: Dict[str, Any] = [
            ele for ele in self.fns if ele["name"] == self.prompt.name][0]
        self.constrained_prompt = "You are a parameter extraction engine.\n"

        self.constrained_prompt += f"User Prompt: {self.prompt.prompt}\n"
        self.constrained_prompt += f"Function to use: {self.prompt.name}"
        params: List[str] = list(target_func["parameters"].keys())
        item: str = "("
        for i in range(len(params)):
            item += f"{params[i]}: "
            ttp: str = target_func["parameters"][params[i]].value
            item += f"{"str" if ttp == "string" else ttp}"
            if i != len(params) - 1:
                item += ", "
        item += ")\n"
        item += "{"
        item += f'"function": "{self.prompt.name}"'

        self.constrained_prompt += item
        self.constrained_prompt += ', "parameters": {'
        para: Dict[str, Any] = ([
            fn for fn in self.fns
            if fn['name'] == self.prompt.name][0]['parameters'])
        j: int = 0
        for key in para:
            self.constrained_prompt += f'"{key}":'
            if (para[key].value == ValidTypes.NUMBER.value):
                self.prompting_number_params(key, para[key].value)
            else:
                self.prompting_str_params(key, para[key].value)
            j += 1
            if (j != len(para)):
                self.constrained_prompt += ", "

    def prompting_str_params(self, key: str, type: str) -> None:
        founded: str = ""
        self.constrained_prompt += '"'
        while True:
            next_word: str = self.generate(self.constrained_prompt + founded)
            if '"' in next_word:
                break
            founded += next_word
        self.prompt.parameters[key] = founded.strip()
        self.constrained_prompt += str(founded).strip() + '"'

    def prompting_number_params(self, key: str, type: str) -> None:
        i: int = 0
        founded: str = ""
        self.constrained_prompt += '" '
        authorized_ids: List[int] = [
            self.tokenizer.encode(ele)[0].tolist()[0] for ele in [" -", " "]]
        next_word: str = self.prompting_by_token(
                self.constrained_prompt + founded, authorized_ids)
        founded += next_word
        while i < self.max_tokens:
            next_word = self.prompting_by_token(
                self.constrained_prompt + founded,
                self.tokenizer.encode('0123456789"')[0].tolist())
            if (next_word == '"'):
                break
            founded += next_word
            i += 1

        self.constrained_prompt += (founded + '"').strip()
        self.prompt.parameters[key] = float(founded)

    def resolve_prompts(self) -> List[Prompt]:
        return self.prompts

    def generate(self, prompt: str) -> str:
        tokens_id: List[int] = self.tokenizer.encode(prompt)[0].tolist()
        logits: List[float] = self.model.get_logits_from_input_ids(tokens_id)
        max_tokens: List[int] = [int(argmax(tensor(logits)).item())]
        re: Union[List[str], str] = self.tokenizer.decode(max_tokens)
        return re[0] if isinstance(re, List) else re


@lru_cache()
def fun(prompt: str) -> Prompt:
    return Prompt(prompt)
