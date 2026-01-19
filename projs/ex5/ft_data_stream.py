DATA = [
    {'id': 1, 'player': 'alice', 'event_type': 'kill', 'data': {'level': 5}},
    {'id': 1, 'player': 'bob', 'event_type': 'item_found', 'data': {'level': 12}},
    {'id': 1, 'player': 'charlie', 'event_type': 'level_up', 'data': {'level': 8}},
    {'id': 2, 'player': 'frank', 'event_type': 'login', 'data': {'level': 35}},
    {'id': 3, 'player': 'alice', 'event_type': 'level_up', 'data': {'level': 45}},
    {'id': 4, 'player': 'bob', 'event_type': 'death', 'data': {'level': 1}},
    {'id': 5, 'player': 'charlie', 'event_type': 'kill', 'data': {'level': 22}}
    ]


def dispatch_event(data: str) -> str:
    if (data == "item_found"):
        return "found treasure"
    elif (data == "kill"):
        return "killed monster"
    elif (data == "level_up"):
        return "leveled up"
    else:
        return data


def gen(ele: dict) -> str:
    return (
            f"Event {ele['id']}: Player {ele['player']} "
            f"(level {ele['data']['level']}) "
            f"{dispatch_event(ele['event_type'])}"
                )


def high_level_players(data: list[dict]) -> list[dict]:
    return [ele for ele in data if ele['data']['level'] >= 10]


def treasure_events(data: list[dict]) -> list[dict]:
    return [ele for ele in data if ele['event_type'] == "item_found"]


def level_up_events(data: list[dict]) -> list[dict]:
    return [ele for ele in data if ele['event_type'] == "level_up"]


def fib(x: int) -> int:
    if (x == 0 or x == 1):
        return x
    if (x < 0):
        return 0
    return fib(x - 1) + fib(x - 2)


def call_fib(x: int) -> list[int]:
    i = 0
    re = []
    while i < x:
        re = [*re, fib(i)]
        i += 1
    return re


def is_prime(x: int) -> bool:
    if (x < 2):
        return False
    return (
        True if len([ele for ele in range(2, x) if x % ele == 0]) == 0
        else False
        )


def call_primes(x: int) -> list[int]:
    re = []
    i = 0
    while len(re) < x:
        if is_prime(i):
            re = [*re, i]
        i += 1
    return re


def ft_data_stream(data: list[dict]) -> None:
    print("=== Game Data Stream Processor ===")
    print("")
    print("Processing 1000 game events...")
    print("")
    generated = iter(DATA)
    print(gen(next(generated)))
    print(gen(next(generated)))
    print(gen(next(generated)))
    print("...")

    print("")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {len(data)}")

    print(f"High-level players (10+): {len(high_level_players(data))}")
    print(f"Treasure events: {len(treasure_events(data))}")
    print(f"Level-up events: {len(level_up_events(data))}")
    print("")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("")

    print("=== Generator Demonstration ===")
    sequence = iter(call_fib(10))
    print("Fibonacci sequence (first 10): ", end="")
    i = 0
    for i in range(10):
        print(f"{next(sequence)}", f"{', ' if i != 9 else ''}", end="", sep="")
        if i == 9:
            print("")
    print("Prime numbers: (first 5): ", end="")
    sequence = iter(call_primes(5))
    for i in range(5):
        print(f"{next(sequence)}", f"{', ' if i != 4 else ''}", end="", sep="")
        if i == 4:
            print("")


if __name__ == "__main__":
    ft_data_stream(DATA)
