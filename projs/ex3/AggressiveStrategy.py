from ex3.GameStrategy import GameSrategy


class AggressiveStrategy(GameSrategy):
    def __init__(s) -> None:
        s.mana = 10
        s.target = 'Enemy Player'
        s.damage = 8

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        while len(hand) > 0 and sum([card.cost for card in battlefield]) < 5:
            card = hand.pop()
            battlefield.append(card)
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
