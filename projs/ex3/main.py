from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.CardTypes import CardTypes


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
    strategy = AggressiveStrategy()
    fantasyCard = FantasyCardFactory()
    re = engine.configure_engine(fantasyCard, strategy)
    for k, v in re.items():
        print(f"{k}: {v}")
    print()
    add = fantasyCard.get_card(CardTypes.CREATURE)
    add("Fire Dragon")
    add = fantasyCard.get_card(CardTypes.CREATURE)
    add("Goblin Warrior")
    add = fantasyCard.get_card(CardTypes.SPELL)
    add("Lightning Bolt")

    print("Simulating aggressive turn...")
    hand = engine.simulate_turn()['Hand']
    print("Hand: ", end="")
    format_hand([f"{ele.name} ({ele.cost})" for ele in hand])
    print()
    battlefield = []
    strategy.execute_turn(hand, battlefield)
    turn2 = strategy.execute_turn(hand, battlefield)
    format_turn(turn2)
    print()

    print("Game Report: ")
    print(engine.get_engine_status())
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


main() if __name__ == "__main__" else None
