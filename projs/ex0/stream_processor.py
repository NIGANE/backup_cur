from typing import Any, List, Dict, Union, Optional
from abc import ABCMeta, abstractmethod


class DataProcessor(metaclass=ABCMeta):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):

    def __init__(self):
        print("Initializing Numeric Processor...")

    def process(self, data: List) -> str:
        print(data)

    def validate(self, data: List) -> bool:
        try:
            for ele in data:
                int(ele)
        except Exception:
            return False
        else:
            return True

    def format_output(self, result: str) -> str:
        pass


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass
