from src.models.Hub import Hub
from typing import List
from src.models.Error import MyError


class Dron:
    def __init__(self, i: int, station: Hub):
        self.name: str = f"D{i}"
        self.is_flying: bool = False
        self.is_reached: bool = False
        self.station: Hub = station
        self.path: List[Hub] = []
        self.index: int = 0

    def set_path(self, path: List[Hub]) -> None:
        self.path = path

    def next_zone(self) -> Hub:
        if len(self.path) > self.index:
            return self.path[self.index]
        raise MyError(
            f"Error: no solution path found for this drone [{self.name}]")

    def prev_zone(self) -> Hub:
        if len(self.path) > self.index:
            return self.path[self.index - 1]
        raise MyError(
            f"Error: no solution path found for this drone [{self.name}]")

    def setp(self) -> None:
        self.prev_zone().pop(self)
        self.next_zone().append(self)
        self.index += 1

    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"[{'flying' if self.is_flying else "in"}"
            f" {self.station.name}]")
