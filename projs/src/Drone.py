from src.models.Hub import Hub
from typing import List
from src.models.Error import MyError
from src.models.Connection import Connection


class Drone:
    def __init__(self, i: int, station: Hub):
        self.name: str = f"D{i}"
        self.is_flying: bool = False
        self.is_reached: bool = False
        self.station: Hub = station
        self.path: List[Hub] = []
        self.index: int = 0

    def set_path(self, path: List[Hub]) -> None:
        self.path = path

    def cur_zone(self) -> Hub:
        return self.path[self.index]

    def next_zone(self) -> Hub:
        if len(self.path) > self.index:
            return self.path[self.index + 1]
        raise MyError(
            f"Error: no solution path found for this drone [{self.name}]")

    def prev_zone(self) -> Hub:
        if len(self.path) > self.index:
            return self.path[self.index - 1]
        raise MyError(
            f"Error: no solution path found for this drone [{self.name}]")

    def step(self) -> None:
        self.cur_zone().pop(self)
        self.next_zone().append(self)
        self.index += 1
        if self.cur_zone() == self.path[-1]:
            self.is_reached = True
        self.station = self.cur_zone()

    def link_opened(self, connections: List[Connection]) -> bool:
        cur = self.cur_zone()
        next = self.next_zone()
        cur_connection: Connection = [con for con in connections
                                      if con.hub1 == cur.name
                                      and con.hub2 == next.name][0]
        if cur_connection.max_lint == cur_connection.per_turn:
            return False
        cur_connection.per_turn += 1
        return True

    def __eq__(self, drone: object) -> bool:
        if not isinstance(drone, Drone):
            return False
        if drone.name == self.name:
            return True
        return False

    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"[{'flying' if self.is_flying else "in"}"
            f" {self.station.name}]")
