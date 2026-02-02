from ex4.TournamentCard import TournamentCard


def format_interfaces(data: list) -> None:
    i = 0
    print("[", end="")
    while i < len(data):
        print(f"{data[i]}", end=f"{'' if i + 1 == len(data) else ', '}")
        i += 1
    print("]")


class TournamentPlatform:

    @staticmethod
    def register_card(card: TournamentCard) -> None:
        print(f"{card.card.name} (ID: {card.card_id})")
        print("Interfaces: ", end="")
        format_interfaces([ele.__name__ for ele in card.interfaces])
        print(f"Rating: {card.rating}")
        print(f"Record: {card.record[0]}-{card.record[1]}")

    def create_match(card1_id: str, card2_id: str) -> None:
        pass

    def get_leaderboard() -> None:
        pass

    def generate_tournament_report() -> None:
        pass
