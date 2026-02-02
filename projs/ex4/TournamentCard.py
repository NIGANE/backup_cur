from ex4 import Rankable
from ex0.Card import Card
from ex2.Combatable import Combatable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(s, id_card: str, card: Card, rating: int) -> None:
        s.card = card
        s.card_id = id_card
        s.interfaces = [Card, Combatable, Rankable]
        s.rating = rating
        s.record = [0, 0]

    def play(self, game_state: dict) -> dict:
        pass

    def attack(s, target) -> dict:
        pass

    def defend(s, incoming_damage: int) -> dict:
        pass

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
