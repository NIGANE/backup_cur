from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    def __init__(s, comb_type: str) -> None:
        s.comb_type = comb_type

    @abstractmethod
    def attack(s, target: Any) -> dict:
        pass

    @abstractmethod
    def defend(s, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(s) -> dict:
        pass
