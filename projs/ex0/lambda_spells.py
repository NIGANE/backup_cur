
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda x: x['power'] >= min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda n: "* " + n + " *", spells)


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda e: e['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


def main() -> None:
    print()
    print("Testing artifact sorter...")
    data = [
        {
            "name": "Fire Staff",
            "power": 92
        },
        {
            "name": "Crystal Orb",
            "power": 85
        }
    ]
    s = artifact_sorter(data)
    print(f"{s[0]['name'].title()} ({s[0]['power']} power) "
          f"comes before {s[1]['name'].title()} ({s[1]['power']} power)")

    print()
    names = ['fireball', 'heal', 'shield']
    print("Testing spell transformer...")
    for ele in spell_transformer(names):
        print(ele, end=" ")
    print()


main() if __name__ == "__main__" else ""
