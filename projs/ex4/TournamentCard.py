from ex4 import Rankable
from ex0.Card import Card
from ex2.Combatable import Combatable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(s, id_card: str, card: Card, rating: int) -> None:
        s.card = card
        s.card_id = id_card
        s.interfaces = [Card, Combatable, Rankable]
        s.rating = rating
        s.wins = 0
        s.losses = 0
        s.record = [s.wins, s.losses]


    def play(self, game_state: dict) -> dict:
        return self.card.play()

    def attack(s, target: "TournamentCard") -> dict:
        diff = 16
        s.rating += diff
        target.defend(diff)
        return {
            "attacker": s.card.name,
            "target": target,
            "damage": s.cost,
        }

    def defend(s, incoming_damage: int) -> dict:
        s.rating -= incoming_damage
        return {
            "defender": s.card.name,
            "damage_taken": incoming_damage,
            "damage_blocked": s.rating - incoming_damage,
        }

    def get_combat_stats(s) -> dict:
        pass

    def calculate_rating(self) -> None:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> None:
        pass
