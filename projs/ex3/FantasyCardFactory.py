from enum import Enum
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card
from typing import Callable


global_creatures = [
            {
                "name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
                "attack": 7, "health": 5
                },
            {
                "name": "Goblin Warrior", "cost": 2, "rarity": "Common",
                "attack": 2, "health": 1
                },
            {
                "name": "Ice Wizard", "cost": 4, "rarity": "Rare",
                "attack": 3, "health": 4
                },
            {
                "name": "Lightning Elemental", "cost": 3, "rarity": "Uncommon",
                "attack": 4, "health": 2
                },
            {
                "name": "Stone Golem", "cost": 6, "rarity": "Rare",
                "attack": 5, "health": 8
                },
            {
                "name": "Shadow Assassin", "cost": 3, "rarity": "Uncommon",
                "attack": 5, "health": 2
                },
            {
                "name": "Healing Angel", "cost": 4, "rarity": "Rare",
                "attack": 2, "health": 6
                },
            {
                "name": "Forest Sprite", "cost": 1, "rarity": "Common",
                "attack": 1, "health": 1
                }
        ]

spells = [
            {
                "name": "Lightning Bolt", "cost": 3, "rarity": "Common",
                "effect_type": "damage"
                },
            {
                "name": "Healing Potion", "cost": 2, "rarity": "Common",
                "effect_type": "heal"
                },
            {
                "name": "Fireball", "cost": 4, "rarity": "Uncommon",
                "effect_type": "damage"
                },
            {
                "name": "Shield Spell", "cost": 1, "rarity": "Common",
                "effect_type": "buff"
                },
            {
                "name": "Meteor", "cost": 8, "rarity": "Legendary",
                "effect_type": "damage"
                },
            {
                "name": "Ice Shard", "cost": 2, "rarity": "Common",
                "effect_type": "damage"
                },
            {
                "name": "Divine Light", "cost": 5, "rarity": "Rare",
                "effect_type": "heal"
                },
            {
                "name": "Magic Missile", "cost": 1, "rarity": "Common",
                "effect_type": "damage"
                },
        ]

artifacts = [
            {
                "name": "Mana Crystal", "cost": 2, "rarity": "Common",
                "durability": 5,
                "effect": "Permanent: +1 mana per turn"
                },
            {
                "name": "Sword of Power", "cost": 3, "rarity": "Uncommon",
                "durability": 3,
                "effect": "Permanent: +2 attack to equipped creature"
                },
            {
                "name": "Ring of Wisdom", "cost": 4, "rarity": "Rare",
                "durability": 4,
                "effect": "Permanent: Draw an extra card each turn"
                },
            {
                "name": "Shield of Defense", "cost": 5, "rarity": "Rare",
                "durability": 6,
                "effect": "Permanent: +3 health to all friendly creatures"
                },
            {
                "name": "Crown of Kings", "cost": 7, "rarity": "Legendary",
                "durability": 8,
                "effect": "Permanent: +1 cost reduction to all cards"
                },
            {
                "name": "Boots of Speed", "cost": 2, "rarity": "Uncommon",
                "durability": 2,
                "effect": "Permanent: Cards cost 1 less mana"
                },
            {
                "name": "Cloak of Shadows", "cost": 3, "rarity": "Uncommon",
                "durability": 3,
                "effect": "Permanent: Creatures have stealth"
                },
            {
                "name": "Staff of Elements", "cost": 6, "rarity": "Legendary",
                "durability": 7,
                "effect": "Permanent: +1 spell damage"
                },
        ]

cards = {
    "Fire Dragon": {
        "cost": 5,
        "rarity": "rare",
        "attack": 3,
        "health": 8
        },
    "Goblin Warrior": {
        "cost": 2,
        "rarity": "rare",
        "attack": 5,
        "health": 4
        },
    "Lightning Bolt": {
        "cost": 3,
        "rarity": "rare",
        "effect_type": "damage"
        },
    "Ice Wizard": {
        "cost": 2,
        "rarity": "Common",
        "effect_type": "damage"
    }
}


class SupportedCards(Enum):
    CREATURE = ['dragon', 'goblin']
    SPELL = ["fireball"]
    ARTIFACT = ["mana_ring"]


class CardTypes(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class FantasyCardFactory(CardFactory):

    def __init__(s):
        s._register = {
            CardTypes.SPELL: s.create_spell,
            CardTypes.ARTIFACT: s.create_artifact,
            CardTypes.CREATURE: s.create_creature
        }
        s.types = {
            CardTypes.ARTIFACT: [],
            CardTypes.CREATURE: [],
            CardTypes.SPELL: []
        }
        s.hand = []
        s.total_cards = 0

    def get_card(s, card_type: str) -> Callable:
        if card_type in s._register:
            return s._register[card_type]
        else:
            raise ValueError("the requested card not found")

    def create_creature(s, name_or_power: str | int | None = None) -> Card:
        card = None
        if isinstance(name_or_power, int):
            for ele in global_creatures:
                if (ele['cost'] <= name_or_power):
                    card = CreatureCard(**ele)
            if card is None:
                raise ValueError("Error: target power not exists")
        elif name_or_power is None:
            card = CreatureCard(**global_creatures[0])
        elif isinstance(name_or_power, str):
            card = CreatureCard(name_or_power, **cards[name_or_power])
        else:
            raise ValueError("Error: incorect gived type")
        s.types[CardTypes.CREATURE].append(card)
        s.hand.append(card)
        s.total_cards += 1
        return card

    def create_spell(s, name_or_power: str | int | None = None) -> Card:
        card = None
        if isinstance(name_or_power, int):
            for ele in spells:
                if (ele['cost'] <= name_or_power):
                    card = SpellCard(**ele)
            if card is None:
                raise ValueError("Error: target power not exists")
        elif name_or_power is None:
            card = SpellCard(**spells[0])
        elif isinstance(name_or_power, str):
            card = SpellCard(name_or_power, **cards[name_or_power])
        else:
            raise ValueError("Error: incorect gived type")
        s.types[CardTypes.SPELL].append(card)
        s.hand.append(card)
        s.total_cards += 1
        return card

    def create_artifact(s, name_or_power: str | int | None = None) -> Card:
        card = None
        if isinstance(name_or_power, int):
            for ele in artifacts:
                if (ele['cost'] <= name_or_power):
                    card = ArtifactCard(**ele)
            if card is None:
                raise ValueError("Error: target power not exists")
        elif name_or_power is None:
            card = ArtifactCard(**artifacts[0])
        elif isinstance(name_or_power, str):
            card = ArtifactCard(name_or_power, **cards[name_or_power])
        else:
            raise ValueError("Error: incorect gived type")
        s.types[CardTypes.ARTIFACT].append(card)
        s.hand.append(card)
        s.total_cards += 1
        return card

    def create_themed_deck(self, size: int) -> dict:
        # i = 0
        # deck = Deck()
        # while i < size:
        #     deck.add_card()
        pass

    def get_supported_types(s) -> dict:
        return {
            "creatures": SupportedCards.CREATURE.value,
            "spells": SupportedCards.SPELL.value,
            "artifacts": SupportedCards.ARTIFACT.value
        }
