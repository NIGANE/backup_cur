from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.FantasyCardFactory import CardTypes
from ex3.GameEngine import StrategyTypes
from ex3.GameEngine import FactoryType

def format_hand(data: list) -> None:
    print("[", end="")
    i = 0
    while (i < len(data)):
        print(data[i], end=f"{', ' if i + 1 != len(data) else ''}")
        i += 1
    print("]")


def format_turn(data: dict) -> None:
    for k, v in data.items():
        print(f"{k}: {v}")


def main() -> None:
    print()
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")

    engine = GameEngine()
    strategy = engine.take_strategy(StrategyTypes.AGGRESSIVE)
    factory = engine.take_factory(FactoryType.FANTASY)
    re = engine.configure_engine(factory, strategy)
    for k, v in re.items():
        print(f"{k}: {v}")
    print()
    add = engine.take_card(CardTypes.CREATURE, factory)
    add("Fire Dragon")
    add = engine.take_card(CardTypes.CREATURE, factory)
    add("Goblin Warrior")
    add = engine.take_card(CardTypes.SPELL, factory)
    add("Lightning Bolt")

    print("Simulating aggressive turn...")
    hand = engine.simulate_turn()['Hand']
    print("Hand: ", end="")
    format_hand([f"{ele.name} ({ele.cost})" for ele in hand])
    print()
    battlefield = []
    turn = strategy.execute_turn(hand, battlefield)
    format_turn(turn)
    print()

    print("Game Report: ")
    print(engine.get_engine_status())
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


main() if __name__ == "__main__" else None
