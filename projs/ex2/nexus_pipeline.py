from typing import Any, List, Union, Optional, Dict, Protocol
from abc import ABC, abstractmethod


class ProcessingPipeline(ABC):
    def __init__(self, stages: List[Any]) -> None:
        self.stages = stages

    def add_stage(self) -> Any:
        pass

    @abstractmethod
    def process(self) -> Any:
        pass


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage():
    def process(self, data: Any) -> Any:
        pass


class TransformStage():
    def process(self, data: Any) -> Any:
        pass


class OutputStage():
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(self) -> Any:
        pass


class CSVAdapter(ProcessingPipeline):
    def process(self) -> Any:
        pass


class StreamAdapter(ProcessingPipeline):
    def process(self) -> Any:
        pass


class NexusManager():
    pass

