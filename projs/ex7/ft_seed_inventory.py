def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    txt = seed_type.capitalize()
    if (unit == "area"):
        unit = "square meters"
    elif (unit == "grams"):
        unit = "grams total"
    elif (unit == "packets"):
        unit = "packets available"
    else:
        print("Unknown unit type")
        return
    print(f"{txt} seeds: {quantity} {unit}")
