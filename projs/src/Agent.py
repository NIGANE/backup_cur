from llm_sdk import Small_LLM_Model
import torch
from typing import List, Any, Dict
from src.models.FunctionDefinition import ValidTypes


class Agent():
    def __init__(
            self, model: Small_LLM_Model, prompt: str,
            functions_definitions):
        self.fns = functions_definitions
        self.fn_names = [fn['name'] for fn in self.fns]
        self.model = model
        self.prompt = prompt
        self.constrained_prompt = ""
        self.encoded_prompt = self.model.encode(self.prompt)[0].tolist()
        self.res: Dict[str, Any] = {}
        self.fn_name_res: str = ""
        self.params: Dict[str, Any] = {}

    def generate_json_valid(self):
        # constrained decoding the function name
        self.generate_function_name()
        selected_fn = [
            fn for fn in self.fns if fn['name'] == self.fn_name_res][0]

        if (self.fn_name_res in self.fn_names):
            self.res["name"] = self.fn_name_res
        else:
            self.res["name"] = "undefined"
        # ///////////////

        # # generating the params
        if (
            self.fn_name_res in self.fn_names and
            selected_fn['parameters'] is not None
        ):
            self.generate_params()
            self.res["parameters"] = self.params
        elif selected_fn['parameters'] is None:
            self.res["parameters"] = "None"
        return ({"prompt": self.prompt, **self.res})

    def generate(self, authorized_strings: List[str]):
        logits = self.model.get_logits_from_input_ids(self.encoded_prompt)
        torch_logits = torch.tensor(logits)
        mask = torch.full(torch_logits.shape, float('-inf'))

        allowed_ids = []
        for word in authorized_strings:
            word_ids = self.model.encode(word)[0].tolist()
            if len(word_ids) == 1:
                allowed_ids.append(word_ids[0])
                mask[word_ids[0]] = 0.0
            else:
                print("warning encoding produces more than one token!!")

        filtered_logits = torch_logits + mask
        next_token_id = torch.argmax(filtered_logits).item()
        return self.model.decode(torch.tensor(next_token_id))

    def generate_function_name(self) -> str:
        authorized_ids = [
            self.model.encode(fn_name).tolist()[0]
            for fn_name in self.fn_names
            ]
        self.constrained_prompt += (
            "the name of the function to use "
            f"for this case: '{self.prompt}' is :")
        i: int = 0
        while (i < self.max_tokenized(authorized_ids)):
            res = self.prompting_by_token([ele[i] for ele in authorized_ids])
            self.fn_name_res += res
            self.constrained_prompt += res
            authorized_ids = self.filter_authorized_ids(self.fn_name_res)
            i += 1
        return self.fn_name_res

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

    def prompting_by_token(self, tokens: List[int]):
        prompt_ids = self.model.encode(self.constrained_prompt)[0].tolist()
        logits = self.model.get_logits_from_input_ids(prompt_ids)
        torch_logits = torch.tensor(logits)
        mask = torch.full(torch_logits.shape, float('-inf'))
        for ele in tokens:
            mask[ele] = 0.0
        filtered_logits = torch_logits + mask
        next_token_id = torch.argmax(filtered_logits).item()
        return self.model.decode(torch.tensor(next_token_id))

    def generate_params(self):
        target_func = [ele for ele in self.fns if ele["name"] == self.fn_name_res][0]
        self.constrained_prompt = f"""You are a parameter extraction engine.
Function: {self.fn_name_res}
Description: {target_func["description"]}
User prompt: '{self.prompt}'
paramters:
"""
        params = [
            fn for fn in self.fns
            if fn['name'] == self.fn_name_res][0]['parameters']
        for key in params:
            self.constrained_prompt += f"{key} ({params[key].value}):  "
            self.prompting_params(key, params[key].value)

    def prompting_params(self, key, tp):
    
        input_ids = self.model.encode(self.constrained_prompt).tolist()[0]
        logits = self.model.get_logits_from_input_ids(input_ids)
        next_word_id = (torch.argmax(torch.tensor(logits)).item())
        next_word = self.model.decode(next_word_id)
        if tp == ValidTypes.INT.value:
            next_word = int(next_word)
        elif tp == ValidTypes.NUMBER.value:
            next_word = float(next_word)
        self.params[key] = next_word
        self.constrained_prompt += str(next_word) + "\n"
        print(self.constrained_prompt)
