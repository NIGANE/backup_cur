from ex4.TournamentCard import TournamentCard


def format_interfaces(data: list) -> None:
    i = 0
    print("[", end="")
    while i < len(data):
        print(f"{data[i]}", end=f"{'' if i + 1 == len(data) else ', '}")
        i += 1
    print("]")


def fn(item: TournamentCard) -> int:
    return item.rating



class TournamentPlatform:
    def __init__(s) -> None:
        s.cards = []
        s.last_winer = None
        s.last_loser = None
        s.leader_bord = []

    def register_card(s, card: TournamentCard) -> None:
        print(f"{card.card.name} (ID: {card.card_id})")
        print("- Interfaces: ", end="")
        format_interfaces([ele.__name__ for ele in card.interfaces])
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.record[0]}-{card.record[1]}")
        s.cards.append(card)
        s.leader_bord = sorted(s.cards, fn(card))

    def create_match(s, card1_id: str, card2_id: str) -> dict:
        card1 = [ele for ele in s.cards if ele.card_id == card1_id][0]
        card2 = [ele for ele in s.cards if ele.card_id == card2_id][0]
        if (card1.rating > card2.rating):
            card1.attack(card2)
            winner = card1
            loser = card2
        else:
            card2.attack(card1)
            winner = card2
            loser = card1
        return {
            "winner": winner.card.name,
            "loser": loser.card.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        } 

    def get_leaderboard(self) -> list:
        return (self.leader_bord)

    def generate_tournament_report() -> None:
        pass
