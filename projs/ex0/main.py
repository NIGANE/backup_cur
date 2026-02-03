from ex0.CreatureCard import CreatureCard


def main() -> None:

    print()
    print("=== DataDeck Card Foundation ===")
    print()

    new_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard info:")
    print(new_card.get_card_info())
    print()
    play_data = {"mana": 6, "effect": "Creature summoned to battlefield"}
    print(f"Playing {new_card.name} with {play_data['mana']} mana available:")
    re = new_card.play(play_data)
    print(f"Playable: {new_card.is_playable(play_data['mana'])}")
    print(f"Play result: {re}")
    print()
    card_target = CreatureCard("Goblin Warrior", 5, "rare", 7, 5)
    print(f"{new_card.name} attacks {card_target.name}")
    res_attack = new_card.attack_target(card_target)
    print(f"Attack result: {res_attack}")
    print()

    fault_data = {
        "effect": "Permanent: +1 mana per turn", "mana": 3
    }
    print(f"Testing insufficient mana ({fault_data['mana']} available):")
    try:
        card_target.play(fault_data)
    except ValueError:
        pass
    print(f"Playable: {card_target.is_playable(fault_data['mana'])}")
    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
