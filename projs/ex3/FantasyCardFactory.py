from enum import Enum
from ex1.Deck import Deck
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card

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
        "attack": 6,
        "health": 4
        },
    "Lightning Bolt": {
        "cost": 3,
        "rarity": "rare",
        "effect_type": "damage"
        },
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

    def get_card(s, card_type: str) -> Card:
        if card_type in s._register:
            return s._register[card_type]
        else:
            raise ValueError("the requested card not found")

    def create_creature(s, name_or_power: str | int | None = None) -> Card:
        card = CreatureCard(name_or_power, **cards[name_or_power])
        s.types[CardTypes.CREATURE].append(card)
        s.hand.append(card)
        s.total_cards += 1
        return card

    def create_spell(s, name_or_power: str | int | None = None) -> Card:
        card = SpellCard(name_or_power, **cards[name_or_power])
        s.types[CardTypes.SPELL].append(card)
        s.hand.append(card)
        s.total_cards += 1
        return card

    def create_artifact(s, name_or_power: str | int | None = None) -> Card:
        card = ArtifactCard(name_or_power, **cards[name_or_power])
        s.types[CardTypes.ARTIFACT].append(card)
        s.hand.append(card)
        s.total_cards += 1
        return card

    def create_themed_deck(self, size: int) -> dict:
        i = 0
        deck = Deck()
        while i < size:
            deck.add_card()

    def get_supported_types(s) -> dict:
        return {
            "creatures": SupportedCards.CREATURE.value,
            "spells": SupportedCards.SPELL.value,
            "artifacts": SupportedCards.ARTIFACT.value
        }
