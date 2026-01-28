from .elements import create_fire, create_water, create_air, create_earth


def healing_potion():
    return (
        f"Healing potion brewed with "
        f"{create_fire()} and {create_water()}"
        )


def strength_potion():
    return (
        f"Strength potion brewed with "
        f"{create_earth()} and {create_fire()}"
        )


def invisibility_potion():
    return (
        f"Invisibility potion brewed with "
        f"{create_air()} and {create_water()}"
        )


def wisdom_potion():
    return (
        f"Wisdom potion brewed with all elements: "
        f"{create_water()} {create_fire()} {create_earth()} {create_air}"
        )
