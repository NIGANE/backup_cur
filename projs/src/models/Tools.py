from typing import Any, List
from src.Drone import Drone
from src.models.Hub import Hub


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
            print(
                f"- {dr.name} [{dr.cur_zone().name}]"
                f"{" => Fly-in" if dr.is_flying else ""}")

    @staticmethod
    def fetch_paths(paths: List[Hub]) -> None:
        for path in paths:
            for zone in path:
                print("*", zone.name, f"({zone.capacity})", end=" ")
            print("\n")