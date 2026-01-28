def validate_ingredients(ingredients: str) -> str:
    return (
        f"{ingredients} - VALID"
        if "fire" in ingredients
        or "water" in ingredients
        or "earth" in ingredients
        or "air" in ingredients
        else f"{ingredients} - INVALID"
        )
