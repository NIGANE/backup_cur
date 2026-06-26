
from llm_sdk import Small_LLM_Model
from torch import torch, Tensor
from typing import Dict, List, Optional, Union, Tuple
from json import load

from src.models.ErrorHandler import MyError


class Tokenization:
    """Encode and decode text using the model's tokenizer vocabulary.

    This class implements a Byte Pair Encoding (BPE)-style tokenizer based on
    the vocabulary and merge rules associated with a language model. It
    converts text into token IDs for inference and reconstructs text from
    token IDs after generation.

    Attributes:
        model: The language model providing the tokenizer resources.
        int_vocab: Mapping from token IDs to their string representations.
        str_vocab: Mapping from token strings to their corresponding IDs.
        space_token_id: Token ID representing a space character.
        new_line_token_id: Token ID representing a newline character.
        priority: Mapping of merge pairs to their priority rank.
        encoding: The current token sequence during BPE encoding.
        token_ids: The encoded token IDs.
    """
    def __init__(self, model: Small_LLM_Model):
        """Initialize the tokenizer.

        Loads the tokenizer vocabulary and merge rules from the supplied
        language model.

        Args:
            model: The language model exposing the tokenizer files.
        """
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
        """Load the tokenizer merge rules.

        Reads the merge file associated with the language model and builds the
        priority table used during Byte Pair Encoding.

        Raises:
            MyError: If the merge file cannot be read or parsed.
        """
        file_path: str = self.model.get_path_to_merges_file()
        try:
            with open(file_path, "r") as f:
                data = f.readlines()
                self.priority = self.load_priority(data)
        except BaseException as e:
            raise MyError(f"Error: {e}")

    def get_vocab(self) -> None:
        """Load the tokenizer vocabulary.

        Reads the tokenizer vocabulary and constructs both token-to-ID and
        ID-to-token mappings.

        Raises:
            MyError: If the vocabulary file cannot be read or parsed.
        """
        try:
            file_path: str = self.model.get_path_to_vocab_file()
            with open(file_path, "r") as f:
                data = load(f)
                self.str_vocab = data
                self.int_vocab = {v: k for k, v in self.str_vocab.items()}
        except BaseException as e:
            raise MyError(f"Error: {e}")

    def encode(self, prompt: str) -> Tensor:
        """Encode a prompt into token IDs.

        The prompt is first normalized by replacing spaces and newline
        characters with their corresponding tokenizer symbols. Merge rules are
        then applied iteratively until no additional merges are possible.

        Args:
            prompt: The input text to tokenize.

        Returns:
            A tensor containing the encoded token IDs.
        """
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
