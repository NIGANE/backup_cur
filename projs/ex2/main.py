from ex2 import ElitCard


def main() -> None:

    print()
    print("=== DataDeck Ability System ===")
    print()
    card = ElitCard("Arcane Warrior", 5, "melee", 9)

    print("EliteCard capabilities:")
    for card_type, methods in card.capable.items():
        print(f"- {card_type}: {methods}")
    print()
    played = card.play({})
    print(
        f"Playing {played['name'].title()} "
        f"({played['type'].title()} Card):"
        )
    print()

    print("Combat phase:")
    print(f"Attack result: {card.attack('Enemy')}")
    print(f"Defense result: {card.defend(2)}")
    print()

    print("Magic phase:")
    print(f"Spell cast: {card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {card.channel_mana(3)}")
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
