
def record_spell(spell_name: str, ingredients: str) -> str:
    from ..grimoire import validate_ingredients
    re = (
        f"Spell recorded: {spell_name} ({validate_ingredients(ingredients)})"
        if "INVALID" not in validate_ingredients(ingredients)
        else
        f"Spell rejected: {spell_name} ({validate_ingredients(ingredients)})"
        )
    return re
