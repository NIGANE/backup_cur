from llm_sdk import Small_LLM_Model
from torch import Tensor, argmax, tensor, full
from typing import List, Any, Dict, Union
from functools import reduce

from src.models.FunctionDefinition import ValidTypes
from src.models.Tokenization import Tokenization
from src.models.Prompt import Prompt
from src.tools.tools import _cache


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
            self.prompt: Prompt = _cache(prompt.lower())
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
                or self.prompt.name == "fn_undefined"):
            self.prompt.name = "fn_undefined"
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
                    item += f"{fn['parameters'][params[i]].value}"
                    if i != len(params) - 1:
                        item += ", "
            item += f"): {fn['description']}\n"
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
            f"'{self.prompt.prompt if self.prompt.prompt else 'empty'}' is :")
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
            item += f"{'str' if ttp == 'string' else ttp}"
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
