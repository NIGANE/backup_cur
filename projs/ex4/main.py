from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.FantasyCardFactory import CardTypes


def main() -> None:
    print()
    print("=== DataDeck Tournament Platform ===")
    print()

    print("Registering Tournament Cards...")
    card_ = FantasyCardFactory().get_card(CardTypes.CREATURE)("Fire Dragon")
    tourn_card = TournamentCard("dragon_001", card, 1200)
    platform = TournamentPlatform()
    platform.register_card(tourn_card)




main() if __name__ == "__main__" else None
