from llm_sdk import Small_LLM_Model
import torch
from typing import List


class Agent():
    def __init__(
            self, model: Small_LLM_Model, prompt: str,
            functions_definitions: List[str]):
        self.fns = functions_definitions
        self.model = model
        self.prompt = prompt
        self.res = ""

    def generate_json_valid(self):
        self.generate(["{"])
        self.generate(['"'])
        self.generate(["name"])
        self.generate(['"'])
        self.generate([":"])
        self.generate([' "'])
        self.generate(['func'])
        self.generate(['"'])
        self.generate([","])
        self.generate([' "'])

        # self.complext_generation([*self.fns])
        self.generate(["}"])
        # while (self.res[-1] != "}"):

    def generate(self, authorized_strings: List[str]):
        prompt_ids = self.model.encode(self.prompt)[0].tolist()

        logits = self.model.get_logits_from_input_ids(prompt_ids)
        logits = torch.tensor(logits)
        mask = torch.full(logits.shape, float('-inf'))

        allowed_ids = []
        for word in authorized_strings:
            word_ids = self.model.encode(word)[0].tolist()
            if len(word_ids) == 1:
                allowed_ids.append(word_ids[0])
                mask[word_ids[0]] = 0.0
            else:
                print("warning encoding produces more than one token!!")

        filtered_logits = logits + mask
        next_token_id = torch.argmax(filtered_logits).item()
        print(f"Predicted word:{self.model.decode([next_token_id])}")
        self.res = self.res + self.model.decode([next_token_id])

    def complext_generation(self, authorized_strings: List[str]):
        pass


# def prompting():
#     agent.generate_json_valid()
#     print(f"res: {agent.res}")
    # authorized_strings = ["fn_add", "fn_subtract", "fn_multiply", "fn_divide"]




    # prompt = "What is the sum of 2 and 3?"
    # authorized_strings = ["fn_add", "fn_subtract", "fn_multiply", "fn_divide"]

    # # encode each authorized string as a sequence of tokens
    # authorized_token_sequences = []
    # for s in authorized_strings:
    #     tokens = model.encode(" " + s)   # e.g. [24944, 62, 2860]
    #     authorized_token_sequences.append(tokens)
    #     print(f"'{s}' → {tokens}  (len: {len(tokens)})")

    # # now do prefix-guided decoding
    # input_ids = model.encode(prompt)
    # generated = []   # tokens generated so far

    # # keep going until all sequences are eliminated or one is fully matched
    # candidates = list(range(len(authorized_strings)))  # indices of still-valid strings

    # for position in range(max(len(s) for s in authorized_token_sequences)):

    #     # which first tokens are still valid at this position?
    #     allowed_at_position = set()
    #     for i in candidates:
    #         seq = authorized_token_sequences[i]
    #         if position < len(seq):
    #             allowed_at_position.add(seq[position])

    #     # get logits for current input
    #     logits = torch.tensor(model.get_logits_from_input_ids(input_ids[0].tolist() + generated))

    #     # mask everything except allowed tokens at this position
    #     mask = torch.full(logits.shape, float('-inf'))
    #     for token_id in allowed_at_position:
    #         mask[token_id] = 0

    #     # pick best token
    #     constrained_logits = logits + mask
    #     next_token = torch.argmax(constrained_logits).item()
    #     generated.append(next_token)

    #     # eliminate candidates that don't match what we just picked
    #     candidates = [
    #         i for i in candidates
    #         if position < len(authorized_token_sequences[i])
    #         and authorized_token_sequences[i][position] == next_token
    #     ]

    #     # if only one candidate left and it's fully generated → done
    #     if len(candidates) == 1:
    #         seq = authorized_token_sequences[candidates[0]]
    #         if len(generated) >= len(seq):
    #             break

    #     # decode result
    #     result = model.decode(input_ids + generated)
    #     print(result)
    #     # → "What is the sum of 2 and 3? fn_add"
