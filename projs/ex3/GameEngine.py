from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameSrategy


class GameEngine:
    def __init__(s):
        s.strategy = None
        s.factory = None
        s.battlefield = []
        s.turns = 0

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
