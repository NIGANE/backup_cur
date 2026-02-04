from ex0 import Card, CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        if (isinstance(card, Card)):
            self.cards.append(card)
        else:
            raise ValueError(
                "Error: the provided card not belongs to Card items"
                )

    def remove_card(self, card_name: str) -> bool:
        for ele in self.cards:
            if ele.name == card_name:
                self.cards.remove(ele)
                return True
        return False

    def shuffle(self) -> None:
        self.cards = [*{*self.cards}]

    def draw_card(self) -> Card:
        if len(self.cards) > 0:
            re = self.cards[0]
            self.remove_card(re.name)
            return re
        else:
            raise ValueError("Error: Deck is empty")

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
        avg_cost = (
            (sum([ele.cost for ele in self.cards]) + 2) / len(self.cards)
            )
        return {
            "total_cards": len(self.cards),
            "creatures": crea,
            "spells": spells,
            "artifacts": art,
            "avg_cost": avg_cost
        }
