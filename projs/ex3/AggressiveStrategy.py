from ex3.GameStrategy import GameSrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card
from typing import List


def calc_damage(battle: List[Card]) -> int:
    total_damage = 0
    for card in battle:
        if isinstance(card, CreatureCard):
            total_damage += card.attack
        if isinstance(card, SpellCard) or isinstance(card, ArtifactCard):
            total_damage += card.cost
    return total_damage


class AggressiveStrategy(GameSrategy):
    def __init__(s) -> None:
        s.target = 'Enemy Player'
        s.damage = 0

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        while len(hand) > 0 and sum([card.cost for card in battlefield]) < 5:
            card = hand.pop()
            battlefield.append(card)
            self.damage = calc_damage(battlefield)
        return {
            "Strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": [ele.name for ele in battlefield],
                "mana_used": sum([card.cost for card in battlefield]),
                "targets_attacked":
                [*self.prioritize_targets([self.target])],
                "damage_dealt": self.damage
            }
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        if self.target in available_targets:
            return [self.target]
        else:
            return [available_targets[0]]
