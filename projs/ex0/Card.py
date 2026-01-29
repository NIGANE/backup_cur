from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(s) -> dict:
        return {
            "name": s.name,
            "cost": s.cost,
            "rarity": s.rarity,
        }

    def is_playable(s, available_mana: int) -> bool:
        return available_mana >= s.cost
