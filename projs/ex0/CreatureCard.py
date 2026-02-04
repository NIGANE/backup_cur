from ex0.Card import Card


class CreatureCard(Card):

    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int
            ) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state['mana'])
        if playable:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": 'Creature summoned to battlefield'
            }
        else:
            raise ValueError(
                f"Error: No mana available to play card {self.name}"
                )

    def attack_target(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": self.attack > target.health
        }

    def get_card_info(s) -> dict:
        return {
            **super().get_card_info(),
            "type": s.type,
            "attack": s.attack,
            "health": s.health
            }
