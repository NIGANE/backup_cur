from ex1 import SpellCard, Deck, SpellCard


def main() -> None:

    print()
    print("=== DataDeck Deck Builder ===")
    print()
    deck = Deck()
    print("Building deck with diffrent card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")
    print()

    print("Drawing and playing cards:")
    print()

    print("Drew: Ljightning Bolt (Spell)")
    deck