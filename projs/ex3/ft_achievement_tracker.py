#!/usr/bin/python3
def count(ele: str, data: list[str]) -> int:
    """
    Counts the occurrences of a specific string within a list.

    Args:
        ele: The string achievement to look for.
        data: A list of achievement strings to search through.

    Returns:
        The total number of times the achievement appears in the data.
    """
    count = 0
    for item in data:
        if (ele == item):
            count += 1
    return count


def rare_achivments(data: list[str]) -> set[str]:
    """
    Identifies achievements that appear exactly once across all players.

    Args:
        data: A flattened list of all achievements from all players.

    Returns:
        A set of achievement strings that are unique to a single player.
    """
    rare = []
    for ele in data:
        if count(ele, data) == 1:
            rare.append(ele)
    return set(rare)


def ft_achievement_tracker(data: dict) -> None:
    """
    Processes and displays analytics for player achievements.

    Calculates universal unique achievements, common achievements across all
        players, rare achievements, and specific comparisons between Alice
        and Bob.

    Args:
        data: A dictionary where keys are player names and values are
            lists of their achievement strings.
    """
    my_set = set()
    group = []
    inter = set(data[[*data][0]])
    print("=== Achievement Tracker System ===")
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
    """
    Entry point of the script to initialize sample data and run the tracker.
    """
    data = {
        'alice': ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'],
        'bob': ['first_kill', 'level_10', 'boss_slayer', 'collector'],
        'charlie': ['level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist']
                    }
    ft_achievement_tracker(data)


if (__name__ == "__main__"):
    main()
