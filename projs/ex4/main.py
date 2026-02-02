from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.FantasyCardFactory import CardTypes


def main() -> None:
    print()
    print("=== DataDeck Tournament Platform ===")
    print()

    print("Registering Tournament Cards...")
    card_1 = FantasyCardFactory().get_card(CardTypes.CREATURE)("Fire Dragon")
    card_2 = FantasyCardFactory().get_card(CardTypes.SPELL)("Ice Wizard")
    played_card1 = TournamentCard("dragon_001", card_1, 1200)
    played_card2 = TournamentCard("wizard_001", card_2, 1150)
    platform = TournamentPlatform()

    platform.register_card(played_card1)
    print()

    platform.register_card(played_card2)
    print()

    print("Creating tournament match...")
    # print(played_card1.card_id)
    platform.create_match(played_card1.card_id, played_card2.card_id)


main() if __name__ == "__main__" else None
