#!/usr/bin/python3
def count(ele: str, data: set[str]) -> int:
    count = 0
    for item in data:
        if (ele == item):
            count += 1
    return count


def rare_achivments(data: list[str]) -> set[str]:
    rare = set()
    for ele in data:
        if count(ele, data) == 1:
            rare = {*rare, ele}
    return rare


def ft_achievement_tracker(data: dict) -> None:
    my_set = set()
    group = list()
    inter = set(data[[*data][0]])
    print("=== Achievement Tracker System ===")
    print("")

    for key, value in data.items():
        print(f"Player {key} achievements: {set(value)}")
    print("")

    print("=== Achievement Analytics ===")
    for key in data:
        my_set = my_set.union(set(data[key]))
        inter = inter.intersection(set(data[key]))
        group = [*group, *data[key]]
    print(f"All unique achievements: {my_set}")
    print(f"Total unique achievements: {len(my_set)}")
    print("")

    print(f"Common to all players: {inter}")
    print(f"Rare achievements (1 player): {rare_achivments(group)}")
    print("")

    print(
        f"Alice vs Bob common: "
        f"{set(data['alice']).intersection(set(data['bob']))}"
        )
    print(f"Alice unique: {set(data['alice']).difference(set(data['bob']))}")
    print(f"Bob unique: {set(data['bob']).difference(set(data['alice']))}")


def main() -> None:
    data = {
        'alice': ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'],
        'bob': ['first_kill', 'level_10', 'boss_slayer', 'collector'],
        'charlie': ['level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist']
                    }
    ft_achievement_tracker(data)


if (__name__ == "__main__"):
    main()
