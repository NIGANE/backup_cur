from llm_sdk.llm_sdk import Small_LLM_Model
from torch import Tensor, argmax, tensor, full
from typing import List, Any, Dict, Union
from functools import reduce

from src.models.FunctionDefinition import ValidTypes
from src.models.Tokenization import Tokenization
from src.models.Prompt import Prompt
from src.tools.tools import _cache


class Agent():
    """Resolve user prompts into function calls using constrained decoding.

        This class orchestrates the constrained decoding pipeline by selecting
        the most appropriate function for each prompt and extracting its
        parameters. It interacts with the language model at the token level to
        ensure that generated outputs conform to the available function
        definitions.

    Attributes:
        fns: The available function definitions, including the fallback
            ``fn_undefined``.
        fn_names: The names of all available functions.
        model: The language model used for inference.
        constrained_prompt: The prompt currently used for constrained
            decoding.
        max_tokens: The maximum number of tokens generated for constrained
            decoding steps.
        prompts: The resolved prompts.
        tokenizer: The tokenizer associated with the language model.
    """
    def __init__(
            self, model: Small_LLM_Model, prompts: List[str],
            functions_definitions: List[Dict]) -> None:
        """Initialize the agent and resolve the supplied prompts.

        A fallback function named ``fn_undefined`` is automatically added to
        the available function definitions. Each prompt is processed
        immediately and
        resolved into a function call.

        Args:
            model: The language model used for constrained decoding.
            prompts: The user prompts to resolve.
            functions_definitions: The available function definitions.
        """
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
            self.prompt: Prompt = _cache(prompt)
            print(f"resolving prompt: {self.prompt.prompt}")
            if (not self.prompt.name):
                self.generate_json_valid()
            self.prompts.append(self.prompt)
            self.empty()

    def empty(self) -> None:
        """Reset the constrained prompt state."""
        self.constrained_prompt = ""

    def generate_json_valid(self) -> None:
        """Generate a valid function call for the current prompt.

        The function name is selected using constrained decoding. If the
        selected function accepts parameters, their values are generated
        afterwards.
        """
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
        """Build the prompt describing the available functions.

        Returns:
            A formatted prompt containing the available function signatures and
            descriptions.
        """
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
        """Generate the function name using constrained decoding.

        The language model is restricted to generating only valid function
        names
        from the available function definitions.
        """
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
        """Return the length of the longest token sequence.

        Args:
            tokens: A collection of tokenized sequences.

        Returns:
            The maximum sequence length.
        """
        if len(tokens) == 0:
            return 0
        max_size = len(tokens[0])
        for tok in tokens:
            if len(tok) > max_size:
                max_size = len(tok)
        return max_size

    def filter_authorized_ids(self, pattern: str) -> List[List[int]]:
        """Filter candidate function names by prefix.

        Args:
            pattern: The generated function name prefix.

        Returns:
            The tokenized function names whose names start with the given
            prefix.
        """
        return [
            self.tokenizer.encode(fn_name).tolist()[0]
            for fn_name in self.fn_names
            if fn_name.startswith(pattern)
        ]

    def prompting_by_token(self, ppt: str, tokens: List[int]) -> str:
        """Generate a token from a constrained vocabulary.

        The model logits are masked so that only the supplied token IDs are
        eligible for selection.

        Args:
            ppt: The prompt provided to the language model.
            tokens: The token IDs allowed during decoding.

        Returns:
            The decoded token selected by the language model.
        """
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
        """Generate the parameters for the selected function.

        Parameter values are generated according to the types defined by the
        selected function's schema.
        """
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
            if (para[key].value == ValidTypes.NUMBER.value
                    or para[key].value == ValidTypes.INTEGER.value):
                self.prompting_number_params(key, para[key].value)
            else:
                self.prompting_str_params(key, para[key].value)
            j += 1
            if (j != len(para)):
                self.constrained_prompt += ", "

    def prompting_str_params(self, key: str, type: str) -> None:
        """Generate a string parameter value.

        Args:
            key: The parameter name.
            type: The parameter type.
        """
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
        """Generate a numeric parameter value.

        Args:
            key: The parameter name.
            type: The parameter type.
        """
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
                self.tokenizer.encode('.0123456789"')[0].tolist())
            if (next_word == '"'):
                break
            founded += next_word
            i += 1
        self.constrained_prompt += (founded + '"').strip()
        if (type == ValidTypes.NUMBER.value):
            self.prompt.parameters[key] = float(founded)
        else:
            self.prompt.parameters[key] = int(founded)

    def resolve_prompts(self) -> List[Prompt]:
        """Return the resolved prompts.

        Returns:
            The prompts annotated with the selected function names and
            generated
            parameters.
        """
        return self.prompts

    def generate(self, prompt: str) -> str:
        """Generate the next token without decoding constraints.

        Args:
            prompt: The prompt provided to the language model.

        Returns:
            The generated token.
        """
        tokens_id: List[int] = self.tokenizer.encode(prompt)[0].tolist()
        logits: List[float] = self.model.get_logits_from_input_ids(tokens_id)
        max_tokens: List[int] = [int(argmax(tensor(logits)).item())]
        re: Union[List[str], str] = self.tokenizer.decode(max_tokens)
        return re[0] if isinstance(re, List) else re
