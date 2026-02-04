from ex0.Card import Card


class SpellCard(Card):
    def __init__(
            s, name: str, cost: int, rarity: str, effect_type: str
            ) -> None:
        super().__init__(name, cost, rarity)
        s.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if self.effect_type == 'damage':
            effect = 'Deal 3 damage to target'
        elif self.effect_type == 'heal':
            effect = "healing"
        elif self.effect_type == "buff":
            effect = "+2 attack to equipped creature"
        else:
            effect = self.effect_type
        return {
             'card_played': self.name, 'mana_used': self.cost,
             'effect': effect
            }

    def resolve_effect(self, targets: list) -> dict:
        match self.effect_type:
            case "damage":
                for ele in targets:
                    ele.health -= 3
            case "healing":
                for ele in targets:
                    ele.health += ele.default_health
            case "buff":
                for ele in targets:
                    ele.attack += 2
