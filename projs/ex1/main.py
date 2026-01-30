from ex1 import SpellCard, Deck, ArtifactCard
from ex0 import CreatureCard


def main() -> None:

    print()
    print("=== DataDeck Deck Builder ===")
    print()
    crea = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    spell = SpellCard(
        "Lightning Bolt", 3, "Legendary", "Deal 3 damage to target"
        )
    arti = ArtifactCard(
        "Mana Crystal", 2, "Legandary", 4, "Permanent: +1 mana per turn"
        )
    deck = Deck()

    deck.add_card(crea)
    deck.add_card(spell)
    deck.add_card(arti)

    print("Building deck with diffrent card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")
    print()

    print("Drawing and playing cards:")
    print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
