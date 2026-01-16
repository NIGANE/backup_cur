
def ft_achievement_tracker(data: dict):
    my_set = set()
    print("=== Achievement Tracker System ===")
    for key, value in data.items():
        print(f"Player {key} achievements: {set(value)}")
    print("")
    print("=== Achievement Analytics ===")
    for value in data.values():
        my_set.add(value)
    print(f"All unique achievements: {set()}")


def main() -> None:
    data = {'alice': ['first_blood', 'pixel_perfect', 'speed_runner', 'first_blood', 'first_blood'], 'bob': ['level_master', 'boss_hunter', 'treasure_seeker', 'level_master', 'level_master'], 'charlie': ['treasure_seeker', 'boss_hunter', 'combo_king', 'first_blood', 'boss_hunter', 'first_blood', 'boss_hunter', 'first_blood'], 'diana': ['first_blood', 'combo_king', 'level_master', 'treasure_seeker', 'speed_runner', 'combo_king', 'combo_king', 'level_master'], 'eve': ['level_master', 'treasure_seeker', 'first_blood', 'treasure_seeker', 'first_blood', 'treasure_seeker'], 'frank': ['explorer', 'boss_hunter', 'first_blood', 'explorer', 'first_blood', 'boss_hunter']}
    ft_achievement_tracker(data)


if (__name__ == "__main__"):
    main()