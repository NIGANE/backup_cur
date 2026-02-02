from ex4.TournamentCard import TournamentCard


def format_interfaces(data: list) -> None:
    i = 0
    print("[", end="")
    while i < len(data):
        print(f"{data[i]}", end=f"{'' if i + 1 == len(data) else ', '}")
        i += 1
    print("]")


class TournamentPlatform:
    def __init__(s) -> None:
        s.cards = []

    def register_card(s, card: TournamentCard) -> None:
        print(f"{card.card.name} (ID: {card.card_id})")
        print("- Interfaces: ", end="")
        format_interfaces([ele.__name__ for ele in card.interfaces])
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.record[0]}-{card.record[1]}")
        s.cards.append(card)

    def create_match(s, card1_id: str, card2_id: str) -> dict:
        card1 = [ele for ele in s.cards if ele.card_id == card1_id][0]
        card2 = [ele for ele in s.cards if ele.card_id == card2_id][0]
        print(card1.card.name)
        return {

        } 

    def get_leaderboard() -> None:
        pass

    def generate_tournament_report() -> None:
        pass
