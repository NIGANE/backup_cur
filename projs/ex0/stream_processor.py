from typing import Any, List, Dict, Union, Optional
from abc import ABCMeta, abstractmethod


def ne_sum(data: list[int]) -> int:
    re = 0
    for ele in data:
        re += int(ele)
    return re


def ne_len(data: Union(list[int], str)) -> int:
    re = 0
    for ele in data:
        re += 1
    return re


class DataProcessor(metaclass=ABCMeta):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def __init__(self):
        print("Initializing Numeric Processor...")

    def process(self, data: List) -> Optional[str]:
        print(f"Processing data: {data}")
        if (self.validate(data)):
            print("Validation: Numeric data verified")
            sum = ne_sum(data)
            avg = sum / ne_len(data)
            return super().format_output(
                f"Output: Processed {ne_len(data)} "
                f"numeric values, sum={sum}, avg={avg}"
                )

    def validate(self, data: List) -> bool:
        try:
            for ele in data:
                int(ele)
        except ValueError:
            return False
        else:
            return True


class TextProcessor(DataProcessor):

    def __init__(self):
        print("Initializing Text Processor...")

    def process(self, data: str) -> str:
        print("Processing data: \"{data}\"")
        if self.validate(data):
            print("Validation: Text data verified")
        words = get_words(data)
        count = ne_len(data)
        return super().format_output(f"Processed text: {count} characters, {words} words")

    def validate(self, data: str) -> bool:
        return True

    def format_output(self, result: str) -> str:
        pass


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass
