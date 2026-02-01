from enum import Enum
# from ex3.CardTypes import CardTypes


class SupportedCards(Enum):
    CREATURE = ['dragon', 'goblin']
    SPELL = ["fireball"]
    ARTIFACT = ["mana_ring"]
