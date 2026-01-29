from ex0.Card import Card


class CreatureCard(Card):

    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int
            ) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable([game_state['mana']])
        print(f"Playable: {playable}")
        if playable:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": game_state['effect']
            }

    def attack_target(self, target) -> dict:
        print(f"{self.name} attacks {target['target']}")
        return {
            "attacker": self.name,
            "target": target["target"],
            "damage_dealt": target["damage_dealt"],
            "combat_resolved": target["combat_resolved"]
        }

    def get_card_info(s) -> dict:
        return {
            **super().get_card_info(),
            "type": "Creature",
            "attack": s.attack,
            "health": s.health
            }
