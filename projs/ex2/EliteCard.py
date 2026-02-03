from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class ElitCard(Card, Magical, Combatable):
    def __init__(s, name: str, cost: int, comb_type: str, mana: int) -> None:
        Card.__init__(s, name, cost, "")
        Combatable.__init__(s, comb_type)
        s.capable = {
            "card": ['play', 'get_card_info', 'is_playable'],
            "Combatable": ['attack', 'defend', 'get_combat_stats'],
            "Magical": ['cast_spell', 'channel_mana', 'get_magic_stats']
            }
        s.type = "Elite"
        s.health = s.cost
        s.mana = s.cost

    def attack(s, target: str) -> dict:
        return {
            "attacker": s.name,
            "target": target,
            "damage": s.cost,
            "combat_type": s.comb_type
        }

    def defend(s, incoming_damage: int) -> dict:
        re = {
            "defender": s.name,
            "damage_taken": incoming_damage,
            "damage_blocked": s.health - incoming_damage,
            "still_alive": bool(s.health - incoming_damage)
        }
        s.health -= incoming_damage
        return re

    def get_combat_stats(s) -> dict:
        pass

    def cast_spell(s, spell_name: str, targets: list) -> dict:
        return {
            "caster": s.name,
            "spell": spell_name,
            "targets": targets,
            "still_alive": bool(s.cost),
            "mana_used": s.mana
        }

    def channel_mana(s, amount: int) -> dict:
        s.mana += amount
        return {
            "channeled": amount,
            "total_mana": s.mana
        }

    def get_magic_stats(s) -> dict:
        pass

    def play(s, game_state: dict) -> dict:
        s.mana -= 1
        return {
            "name": s.name,
            "type": s.type
        }
