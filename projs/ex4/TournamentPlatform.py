from typing import List
from ex4.TournamentCard import TournamentCard


def format_interfaces(data: list) -> None:
    i = 0
    print("[", end="")
    while i < len(data):
        print(f"{data[i]}", end=f"{'' if i + 1 == len(data) else ', '}")
        i += 1
    print("]")


def sort(items: List[TournamentCard]) -> List[TournamentCard]:
    for ind in range(len(items)):
        min_index = ind

        for j in range(ind + 1, len(items)):
            if items[j].rating > items[min_index].rating:
                min_index = j

        items[ind], items[min_index] = items[min_index], items[ind]
    return items


class TournamentPlatform:
    def __init__(s) -> None:
        s.cards = []
        s.last_winer = None
        s.last_loser = None
        s.matches = 0

    def register_card(s, card: TournamentCard) -> None:
        print(f"{card.card.name} (ID: {card.card_id})")
        print("- Interfaces: ", end="")
        format_interfaces([ele.__name__ for ele in card.interfaces])
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.record[0]}-{card.record[1]}")
        s.cards.append(card)

    def create_match(s, card1_id: str, card2_id: str) -> dict:
        s.matches += 1
        card1 = [ele for ele in s.cards if ele.card_id == card1_id][0]
        card2 = [ele for ele in s.cards if ele.card_id == card2_id][0]
        if (card1.rating > card2.rating):
            card1.attack(card2)
            card1.wins += 1
            card2.losses += 1
            winner = card1
            loser = card2
        else:
            card2.attack(card1)
            card1.losses += 1
            card2.wins += 1
            winner = card2
            loser = card1
        return {
            "winner": winner.card.name,
            "loser": loser.card.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        return sort(self.cards)

    def generate_tournament_report(s) -> dict:
        avg = (
            sum([ele.get_rank_info()['rating'] for ele in s.cards])
            / len(s.cards)
            )
        return {
            "total_cards": len(s.cards),
            "matches_played": s.matches,
            "avg_rating": int(avg),
            "platform_status": "active"
        }
