from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameSrategy
from enum import Enum
from typing import Callable


class StrategyTypes(Enum):
    AGGRESSIVE = AggressiveStrategy

class FactoryType(Enum):
    FANTASY = FantasyCardFactory

class GameEngine:
    def __init__(s):
        s.strategy = None
        s.factory = None
        s.battlefield = []
        s.turns = 0

    @staticmethod
    def take_factory(str: FactoryType) -> CardFactory:
        return str.value()

    @staticmethod
    def take_card(str: str, factory: CardFactory) -> Callable:
        return factory.get_card(str)

    @staticmethod
    def take_strategy(str: StrategyTypes) -> GameSrategy:
        return str.value()

    def configure_engine(
            s, factory: CardFactory, strategy: GameSrategy
                         ) -> dict:
        s.strategy = strategy
        s.factory = factory
        return {
            "Factory": factory.__class__.__name__,
            "Strategy": strategy.__class__.__name__,
            "available types": factory.get_supported_types()
        }

    def simulate_turn(s) -> dict:
        s.turns += 1
        return {
            "Hand": s.factory.hand
        }

    def get_engine_status(s):
        return {
            "turns_simulated": s.turns,
            "strategy_used": s.strategy.__class__.__name__,
            "total_damage": s.strategy.damage,
            "cards_created": s.factory.total_cards
        }
