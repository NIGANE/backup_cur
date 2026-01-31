from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class ElitCard(Card, Magical, Combatable):
    def __init__(s, name: str, cost: int, comb_type: str, mana: int) -> None:
        Card.__init__(s, name, cost, "")
        Combatable.__init__(s, comb_type)
        Magical.__init__(s, mana)

    def attack(s, target: str) -> dict:
        return {
            "attacker": s.name,
            "target": target,
            "damage": s.cost,
            "combat_type": s.comb_type
        }

    def defend(s, incoming_damage: int) -> dict:
        s.mana -= incoming_damage
        return {
            "defender": s.name,
            "damage_taken": incoming_damage,
            "damage_blocked": s.cost - incoming_damage,
            "still_alive": bool(s.mana)
        }

    def get_combat_stats(s) -> dict:
        pass

    def cast_spell(s, spell_name: str, targets: list) -> dict:
        return {
            "caster": s.name,
            "spell": spell_name,
            "targets": targets,
            "still_alive": bool(s.mana)
        }

    def channel_mana(s, amount: int) -> dict:
        return {
            "channeled": amount,
            "total_mana": s.mana
        }

    def get_magic_stats(s) -> dict:
        pass

    def play(s, game_state: dict) -> dict:
        pass
