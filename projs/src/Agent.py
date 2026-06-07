from llm_sdk import Small_LLM_Model
from torch import Tensor, argmax, tensor, full
from typing import List, Any, Dict
from src.models.FunctionDefinition import ValidTypes
from src.tools.tools import in_string
from functools import reduce


class Prompt():
    def __init__(self, prompt: str):
        self.prompt: str = prompt
        self.name: str = ""
        self.parameters: Dict[str, Any] = {}


class Agent():
    def __init__(
            self, model: Small_LLM_Model, prompts: List[str],
            functions_definitions):
        self.fns = functions_definitions
        self.fn_names = [fn['name'] for fn in self.fns]
        self.model = model
        self.constrained_prompt = ""
        self.max_tokens: int = 5
        self.prompts: List[Prompt] = []
        for prompt in prompts:
            self.prompt = Prompt(prompt)
            print(f"resolving prompt: {self.prompt.prompt}")
            self.generate_json_valid()
            self.prompts.append(self.prompt)
            self.empty()
            res = {
                "name": self.prompt.name,
                "parameters": self.prompt.parameters
                }
            print(f"|-> {res}")
            break

    def empty(self):
        self.constrained_prompt = ""

    def generate_json_valid(self):
        # constrained decoding the function name
        self.generate_function_name()
        selected_fn = [
            fn for fn in self.fns if fn['name'] == self.prompt.name][0]
        if (self.prompt.name not in self.fn_names):
            self.prompt.name = "undefined"
            return

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
            self.model.encode(fn_name).tolist()[0]
            for fn_name in self.fn_names
            ]
        self.constrained_prompt = self.build_prompt()
        self.constrained_prompt += (
            f"the best function to traite "
            f"this user request: '{self.prompt.prompt}' is :")

        i: int = 0
        while (i < self.max_tokenized(authorized_ids)):
            res = self.prompting_by_token(
                self.constrained_prompt, [ele[i] for ele in authorized_ids])
            self.prompt.name += res
            self.constrained_prompt += res
            authorized_ids = self.filter_authorized_ids(self.prompt.name)
            i += 1

    @staticmethod
    def max_tokenized(tokens: List[List[int]]):
        if len(tokens) == 0:
            return 0
        max_size = len(tokens[0])
        for tok in tokens:
            if len(tok) > max_size:
                max_size = len(tok)
        return max_size

    def filter_authorized_ids(self, pattern: str) -> List[List[int]]:
        return [
            self.model.encode(fn_name).tolist()[0]
            for fn_name in self.fn_names
            if fn_name.startswith(pattern)
        ]

    def prompting_by_token(self, ppt: str, tokens: List[int]) -> str:
        prompt_ids = self.model.encode(ppt)[0].tolist()
        logits = self.model.get_logits_from_input_ids(prompt_ids)
        torch_logits = tensor(logits)
        mask = full(torch_logits.shape, float('-inf'))
        for ele in tokens:
            mask[ele] = 0.0
        filtered_logits = torch_logits + mask
        next_token_id = argmax(filtered_logits)
        return self.model.decode(next_token_id)

    def generate_params(self):
        target_func = [
            ele for ele in self.fns if ele["name"] == self.prompt.name][0]
        self.constrained_prompt = (
            f"You are a parameter extraction engine.\n"
            f"User prompt: '{self.prompt.prompt}'\n"
            f"Function used: {self.prompt.name}")
        params = list(target_func["parameters"].keys())
        item = "("
        for i in range(len(params)):
            item += f"{params[i]}: "
            item += f"{target_func.get("parameters")[params[i]].value}"
            if i != len(params) - 1:
                item += ", "
        item += ")\n"
        item += f"Description: {target_func["description"]}\n"
        self.constrained_prompt += item
        params = [
            fn for fn in self.fns
            if fn['name'] == self.prompt.name][0]['parameters']
        for key in params:
            self.constrained_prompt += f"{key} ({params[key].value}):"
            if (params[key].value == ValidTypes.NUMBER.value):
                self.prompting_number_params(key, params[key].value)
            else:
                self.prompting_params(key, params[key].value)

    def prompting_params(self, key: str, type: str) -> None:
        i = 0
        founded = ""
        print(self.constrained_prompt)
        while i < self.max_tokens:
            input_ids = self.model.encode(
                self.constrained_prompt + founded).tolist()[0]
            logits = self.model.get_logits_from_input_ids(input_ids)
            next_word_id: Tensor = (argmax(tensor(logits)))
            next_word = self.model.decode(next_word_id)
            if (next_word == "'\n"):
                break
            if (
                in_string(
                    (founded + next_word.strip()).strip(), self.prompt.prompt)
                    ):
                founded += next_word
            i += 1
        print("fnded: #", founded, "#")
        self.prompt.parameters[key] = founded
        self.constrained_prompt += str(founded) + "\n"

    def prompting_number_params(self, key: str, type: str):
        i: int = 0
        founded: str = ""
        authorized_ids = [
            self.model.encode(ele)[0].tolist()[0] for ele in [" -", " "]]
        next_word = self.prompting_by_token(
                self.constrained_prompt + founded, authorized_ids)
        founded += next_word
        while i < self.max_tokens:
            next_word = self.prompting_by_token(
                self.constrained_prompt + founded,
                self.model.encode("0123456789\n")[0].tolist())
            if (next_word == "'\n"):
                break
            if (
                in_string(
                    (founded + next_word.strip()).strip(), self.prompt.prompt)
                    ):
                founded += next_word
            i += 1
        self.constrained_prompt += founded
        self.prompt.parameters[key] = int(founded)

    def resolve_prompts(self) -> List[Prompt]:
        return self.prompts
