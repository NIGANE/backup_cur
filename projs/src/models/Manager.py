from typing import List
from src.models.Hub import Hub
from src.models.Connection import Connection
from src.models.Error import MyError


class Manager:
    def __init__(self) -> None:
        self.total_drones: int = 0
        self.hubs: List[Hub] = []

    def set_total_drones(self, nb: int) -> None:
        self.total_drones = nb

    def add_hub(self, hub: Hub, line: int) -> None:
        for ele in self.hubs:
            if ele == hub:
                raise MyError(
                    "Error (Invalid configuraions): duplicate hub coordinates"
                    f" from configuration file line: {line}")
        self.hubs.append(hub)

    def resolve_connection(self, con: Connection, line: int):
        if (len([ele for ele in self.hubs if ele.name == con.hub1])
                or len([ele for ele in self.hubs if ele.name == con.hub2])):
            raise MyError(
                "Error (invalid configuration): "
                f"invalid connection hubs at line {line}")
        hub1: Hub = [ele for ele in self.hubs if ele.name == con.hub1][0]
        hub2: Hub = [ele for ele in self.hubs if ele.name == con.hub2][0]
        hub1.connect(hub2, Connection.max_lint)
        hub2.connect(hub1, Connection.max_lint)
