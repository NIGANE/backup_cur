from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
            self, name: str, cost: int, rarity: str, durability: int,
            effect: str
            ) -> None:
        super().__init__(name, cost, rarity)
        self.effect = effect
        self.durability = durability

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name, 'mana_used': self.cost,
            'durability': self.durability,
            'effect': self.effect
                }

    def activate_ability(self) -> dict:
        pass
