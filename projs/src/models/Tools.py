from typing import Any, List
from src.Drone import Drone


class Tools:
    @staticmethod
    def indexof(ele: Any, seq: List[Any]) -> int:
        i: int = 0
        while i < len(seq):
            if seq[i] == ele:
                return i
            i += 1
        return -1

    @staticmethod
    def fetch_drones(drones: List[Drone]) -> None:
        for dr in drones:
            print(f"- {dr.name} [{dr.cur_zone().name}]")
