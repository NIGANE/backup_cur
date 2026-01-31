from abc import ABC, abstractmethod


class Magical(ABC):
    def __init__(s, mana: int) -> None:
        s.mana = mana

    @abstractmethod
    def cast_spell(s, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
