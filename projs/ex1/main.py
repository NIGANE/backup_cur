from ex1 import SpellCard, Deck, ArtifactCard
from ex0 import CreatureCard, Card


def format_drawing(data: Card) -> None:
    type = "Spell" if isinstance(data, SpellCard) else "Artifact"
    state = {'mana': 6}
    print(
        f"Drew: {data.name} "
        f"({'Creature' if isinstance(data, CreatureCard) else type})"
        )
    print(f"Play result: "
          f"{data.play(state)}"
          )


def main() -> None:

    print()
    print("=== DataDeck Deck Builder ===")
    print()
    crea = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    spell = SpellCard(
        "Lightning Bolt", 3, "Legendary", "damage"
        )
    arti = ArtifactCard(
        "Mana Crystal", 2, "Legandary", 4, "Permanent: +1 mana per turn"
        )
    deck = Deck()
    try:
        deck.add_card(spell)
        deck.add_card(arti)
        deck.add_card(crea)
    except ValueError as e:
        print(e)

    print("Building deck with diffrent card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")
    print()

    print("Drawing and playing cards:")
    print()
    card1 = deck.draw_card()
    format_drawing(card1)
    print()
    card2 = deck.draw_card()
    format_drawing(card2)
    print()
    card3 = deck.draw_card()
    format_drawing(card3)
    print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
