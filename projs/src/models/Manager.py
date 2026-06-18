from typing import List, Optional
from src.models.Hub import Hub
from src.models.Connection import Connection
from src.models.Error import MyError
from src.models.Hub import ZoneType


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
        start = [hub for hub in self.hubs if hub.start]
        end = [hub for hub in self.hubs if hub.end]
        if (len(start) > 1):
            raise MyError(
                "Error (Invalid Configuration): duplicate start hub"
                f" at line: {line}"
            )
        if (len(end) > 1):
            raise MyError(
                "Error (Invalid Configuration): duplicate end hub"
                f" at line: {line}"
            )

    def path_finding(self) -> None:
        self.start: Hub = [ele for ele in self.hubs if ele.start][0]
        self.end: Hub = [ele for ele in self.hubs if ele.end][0]
        queue: List[Hub] = [ele for ele in self.hubs if ele.start]
        queue[0].relaxed = queue[0].cost
        while (len(queue) > 0):
            cur: Hub = queue.pop()
            for ele in cur.connections:
                if (ele["hub"].type == ZoneType.BLOCKED):
                    continue
                queue = [ele["hub"], *queue]
            for ele in cur.connections:
                target = ele["hub"]
                if (cur.relaxed + target.cost < target.relaxed):
                    target.relaxed = cur.relaxed + target.cost
        self.resolve_shortest_path()

    def resolve_shortest_path(self) -> None:
        stack: List[Hub] = [self.start]
        cur: Hub = stack[-1]
        while (cur != self.end):
            target = self.get_chepest(cur)
            if (target):
                stack.append(target)
                cur = target
            else:
                stack.pop()
                cur = stack[-1]
        print([ele.name for ele in stack])

    def get_chepest(self, hub: Hub) -> Hub:
        autorized: List[Hub] = [
            ele["hub"] for ele in hub.connections if not ele["hub"].visited
        ]
        min_cost: float = min([ele.relaxed for ele in autorized])
        return [ele for ele in autorized if ele.relaxed == min_cost][0]

    def resolve_connection(self, con: Connection, line: int):
        if (not self.get_by_name(con.hub1)
                or not self.get_by_name(con.hub2)):
            raise MyError(
                "Error (invalid configuration): "
                f"invalid connection hubs at line {line}")
        hub1: Hub = [ele for ele in self.hubs if ele.name == con.hub1][0]
        hub2: Hub = [ele for ele in self.hubs if ele.name == con.hub2][0]
        hub1.connect(hub2, con.max_lint)

    def get_by_name(self, name: str) -> Optional[Hub]:
        for ele in self.hubs:
            if ele.name == name:
                return ele
        return None

    def __str__(self):
        return (f"hubs: {len(self.hubs)} "
                f"total drones: {self.total_drones}"
                )
