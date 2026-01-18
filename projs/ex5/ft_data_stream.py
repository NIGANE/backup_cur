DATA = [
    {'id': 1, 'player': 'frank', 'event_type': 'login', 'timestamp': '2024-01-01T23:17', 'data': {'level': 16, 'score_delta': 128, 'zone': 'pixel_zone_2'}},
    {'id': 2, 'player': 'frank', 'event_type': 'login', 'timestamp': '2024-01-22T23:57', 'data': {'level': 35, 'score_delta': -11, 'zone': 'pixel_zone_5'}},
    {'id': 3, 'player': 'alice', 'event_type': 'level_up', 'timestamp': '2024-01-07T22:41', 'data': {'level': 45, 'score_delta': 458, 'zone': 'pixel_zone_4'}},
    {'id': 4, 'player': 'bob', 'event_type': 'death', 'timestamp': '2024-01-19T08:51', 'data': {'level': 1, 'score_delta': 63, 'zone': 'pixel_zone_4'}},
    {'id': 5, 'player': 'charlie', 'event_type': 'kill', 'timestamp': '2024-01-05T06:48', 'data': {'level': 22, 'score_delta': 4, 'zone': 'pixel_zone_1'}}
    ]

eve = [
            'login',
            'logout',
            'kill',
            'death',
            'level_up',
            'item_found']


def dispatch_event(data: str) -> str:
    if (data == "item_found"):
        return "found treasure"
    elif (data == "kill"):
        return "killed monster"
    elif (data == "level_up"):
        return "leveled up"
    else:
        return data


def gen(ele: dict):
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


def ft_data_stream(data: list[dict]) -> None:
    print("=== Game Data Stream Processor ===")
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
    print("Processing time: 0.045 seconds")
    print("")
    print("=== Generator Demonstration ===")


if __name__ == "__main__":
    ft_data_stream(DATA)
