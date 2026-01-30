from ex0.CreatureCard import CreatureCard


def main() -> None:

    print()
    print("=== DataDeck Card Foundation ===")
    print()

    print("=== DataDeck Card Foundation ===")
    print()

    new_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard info")
    print(new_card.get_card_info())
    re = new_card.play({
        "name": "Mana Crystal",
        "cost": 2, "rarity": "Common", "durability": 5,
        "effect": "Permanent: +1 mana per turn"
        })
    print(f"Play result: {re}")
    print()

    result_attack = new_card.attack_target({
        'target': 'Goblin Warrior',
        'damage_dealt': 7, 'combat_resolved': True
        })
    print(f"Attack result: {result_attack}")
    print(
            f"Playing {self.name} with "
            "6 mana available:"
            )   

if __name__ == "__main__":
    main()