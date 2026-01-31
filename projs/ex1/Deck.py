from ex0 import Card, CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import Generator


def gen_card(data: list[Card]) -> Generator:
    for e in data:
        yield e


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        try:
            if (isinstance(card, Card)):
                self.cards.append(card)
            else:
                raise ValueError(
                    "Error: the provided card not belongs to Card items"
                    )
        except ValueError as e:
            print(e)

    def remove_card(self, card_name: str) -> bool:
        for ele in self.cards:
            if ele.name == card_name:
                self.cards.remove(ele)
                return True
        return False

    def shuffle(self) -> None:
        self.cards = [*{*self.cards}]

    def draw_card(self) -> Card:
        ele = iter(self.cards)
        return ele

    def get_deck_stats(self) -> dict:
        crea = len(
            [ele for ele in self.cards if isinstance(ele, CreatureCard)]
        )
        spells = len(
            [ele for ele in self.cards if isinstance(ele, SpellCard)]
        )
        art = len(
            [ele for ele in self.cards if isinstance(ele, ArtifactCard)]
        )
        avg_cost = sum([ele.cost for ele in self.cards]) / len(self.cards)
        return {
            "total_cards": len(self.cards),
            "creatures": crea,
            "spells": spells,
            "artifacts": art,
            "avg_cost": avg_cost
        }
