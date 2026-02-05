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
        s.attacks = 0
        s.defends = 0
        s.palyed = 0
        s.record = [s.wins, s.losses]

    def play(self, game_state: dict) -> dict:
        self.played += 1
        return self.card.play()

    def attack(s, target: "TournamentCard") -> dict:
        s.attacks += 1
        diff = 16
        s.rating += diff
        target.defend(diff)
        return {
            "attacker": s.card.name,
            "target": target,
            "damage": s.card.cost,
        }

    def defend(s, incoming_damage: int) -> dict:
        s.defends += 1
        s.rating -= incoming_damage
        return {
            "defender": s.card.name,
            "damage_taken": incoming_damage,
            "rating": s.rating - incoming_damage,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attacks": self.attacks,
            "defends": self.defends,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "loses": self.losses
        }
