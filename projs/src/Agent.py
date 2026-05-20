from llm_sdk import Small_LLM_Model
import torch
from typing import List


class Agent():
    def __init__(
            self, model: Small_LLM_Model, prompt: str,
            functions_definitions):
        self.fns = functions_definitions
        self.fn_names = [fn['name'] for fn in self.fns]
        self.model = model
        self.prompt = prompt
        self.constrained_prompt = prompt
        self.encoded_prompt = self.model.encode(self.prompt)[0].tolist()
        self.res = ""
        self.fn_name_res = ""

    def generate_json_valid(self):
        # constrained decoding the function name
        # self.res += '{"name": "'
        self.generate_function_name()

        selected_fn = [
            fn for fn in self.fns if fn['name'] == self.fn_name_res][0]
        # self.res += '"'
        # if (self.fn_name_res in self.fn_names):
        #     self.res += self.fn_name_res
        # else:
        #     self.res += "undefined"
        # self.res += '"'
        # ///////////////

        # generating the params
        if (
            self.fn_name_res in self.fn_names and
            selected_fn['parameters'] is not None
        ):
            self.res += ', "parameters": {'
            self.generate_params()
            self.res += '}'
        elif selected_fn['parameters'] is None:
            self.res += ', "parameters": None'
        self.res += "}"

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
        self.res = self.res + self.model.decode(torch.tensor(next_token_id))

    def generate_function_name(self) -> str:
        authorized_ids = [
            self.model.encode(fn_name).tolist()[0]
            for fn_name in self.fn_names
            ]
        self.constrained_prompt += ", the name of the function is "
        for i in range(len(authorized_ids[0])):
            res = self.prompting_by_token([ele[i] for ele in authorized_ids])
            self.fn_name_res += res
            self.constrained_prompt += res
        # self.res += self.fn_name_res
        return self.fn_name_res

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
        params = [
            fn for fn in self.fns
            if fn['name'] == self.fn_name_res][0]['parameters']
        for key in params:
            print(f"{key} : {params[key]}")
            self.prompting_params(key, params[key])

    def prompting_params(self, key, value):
        print(self.constrained_prompt)