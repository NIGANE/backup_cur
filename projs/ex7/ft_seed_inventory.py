def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    txt = seed_type.capitalize()
    if (unit not in ["packets", "grams", "area"]):
        print("Unknown unit type")
        return
    print(f"{txt} seeds: {quantity} {unit} packets available")
