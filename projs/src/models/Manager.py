from typing import List, Optional
from src.models.Hub import Hub
from src.models.Connection import Connection
from src.models.Error import MyError
from src.models.Hub import ZoneType
# from src.models.Tools import Tools
from src.Drone import Drone


class Manager:
    def __init__(self) -> None:
        self.total_drones: int = 0
        self.hubs: List[Hub] = []
        self.shortest_path: List[Hub] = []
        self.paths: List[List[Hub]] = []
        self.drones: List[Drone] = []
        self.turnes: int = 0
        self.running_sim: bool = False
        self.connections: List[Connection] = []

    def set_endpoints(self) -> None:
        try:
            self.start: Hub = [ele for ele in self.hubs if ele.start][0]
            self.end: Hub = [ele for ele in self.hubs if ele.end][0]
        except Exception:
            raise MyError("Error: no start/end hub founded")

    def get_total_cost(self, path: List[Hub]) -> float:
        total: float = 0
        for ele in path:
            total += ele.cost
        return total

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

    def relaxation(self) -> None:
        queue: List[Hub] = [self.start]
        queue[0].relaxed = queue[0].cost
        while (len(queue) > 0):
            cur: Hub = queue.pop()
            cur.visited = True

            for ele in cur.connections:

                if (ele["hub"].type == ZoneType.BLOCKED):
                    continue
                if (ele["hub"].visited or ele["hub"] in queue):
                    continue
                queue = [ele["hub"], *queue]
            for ele in cur.connections:
                target: Hub = ele["hub"]
                if (cur.relaxed + target.cost < target.relaxed):
                    target.relax_hh(cur)
                    # if target.is_priority():
                    #     target.relax_priority(cur)
        if self.end.relaxed == float("inf"):
            raise MyError("Error: No solution path founded")

    def path_finding(self) -> None:
        self.relaxation()
        self.find_shortest_path()
        self.discover_multiple_paths()
        self.paths_filter_by_cost(
            self.get_total_cost(self.shortest_path) * 1.38)
        if (len(self.paths) > 4):
            self.paths_filter_by_len(len(self.shortest_path) + 2)

    def paths_filter_by_cost(self, min_cost: float) -> None:
        new_list: List[List[Hub]] = []
        for path in self.paths:
            co: float = self.get_total_cost(path)
            if min_cost > co:
                new_list.append(path)
        self.paths = new_list

    def paths_filter_by_len(self, min_len: int) -> None:
        new_list: List[List[Hub]] = []
        for path in self.paths:
            if len(path) <= min_len:
                new_list.append(path)
        self.paths = new_list

    def find_shortest_path(self) -> None:
        cur: Hub = self.end
        while (True):
            self.shortest_path = [cur, *self.shortest_path]
            if cur == self.start:
                break
            cur = cur.prev

    def discover_multiple_paths(self) -> None:
        new_path: Optional[List[Hub]] = self.shortest_path
        while new_path is not None:
            if new_path in self.paths:
                break
            for ele in new_path:
                ele.relaxed += 100.0
            self.paths.append(new_path)
            new_path = self.resolve_new_path()

    def resolve_new_path(self) -> Optional[List[Hub]]:
        self.unvisit()
        stack: List[Hub] = [self.start]
        cur: Hub = stack[-1]
        while (cur != self.end):
            cur.visited = True
            target: Optional[Hub] = self.get_chepest(cur)
            if (target):
                stack.append(target)
                cur = target
            else:
                if cur == self.start:
                    return None
                stack.pop()
                cur = stack[-1]
        if len(stack) < 1:
            return None
        return stack

    def get_chepest(self, hub: Hub) -> Optional[Hub]:
        authorized: List[Hub] = [
            ele["hub"] for ele in hub.connections if not ele["hub"].visited
        ]
        if len(authorized) < 1:
            return None
        prio: Optional[Hub] = self.any_priority(authorized)
        if prio:
            return prio
        min_cost: float = min([ele.relaxed for ele in authorized])
        return [ele for ele in authorized if ele.relaxed == min_cost][0]

    def resolve_connection(self, con: Connection, line: int):
        start_hub = [ele for ele in self.hubs if ele.start]
        end_hub = [ele for ele in self.hubs if ele.end]
        if len(start_hub) == 0:
            raise MyError(
                "Error (invalid configuration): "
                "No start_hub founded"
            )
        if len(end_hub) == 0:
            raise MyError(
                "Error (invalid configuration): "
                "No end_hub founded"
            )
        if not self.get_by_name(con.hub1):
            raise MyError(
                "Error (invalid configuration): "
                f"Unkown connection hub '{con.hub1}' at line {line}")

        if not self.get_by_name(con.hub2):
            raise MyError(
                "Error (invalid configuration): "
                f"Unkown connection hub '{con.hub2}' at line {line}")
        hub1: Hub = [ele for ele in self.hubs if ele.name == con.hub1][0]
        hub2: Hub = [ele for ele in self.hubs if ele.name == con.hub2][0]
        hub1.connect(hub2, con.max_lint)
        self.connections.append(con)

    def get_by_name(self, name: str) -> Optional[Hub]:
        for ele in self.hubs:
            if ele.name == name:
                return ele
        return None

    def any_priority(self, hubs: List[Hub]) -> Optional[Hub]:
        for ele in hubs:
            if ele.type == ZoneType.PRIORITY.value:
                return ele
        return None

    def unvisit(self):
        for hub in self.hubs:
            hub.visited = False

    def __str__(self):
        return (f"hubs: {len(self.hubs)} "
                f"total drones: {self.total_drones}"
                )

    def split_drones(self):
        for ind, ele in enumerate(self.drones):
            ele.set_path(self.paths[(ind + 1) % len(self.paths)])

    def reset_connection_link_capacity(self):
        for con in self.connections:
            con.per_turn = 0

    def run_simulation(self) -> None:
        i: int = 0
        self.running_sim = True
        print("paths: ", len(self.paths))
        while i < self.total_drones:
            drone = Drone(i + 1, self.start)
            self.drones.append(drone)
            i += 1

        self.split_drones()
        while self.running_sim:
            self.turnes += 1
            for drone in self.drones:
                if drone.is_reached:
                    continue
                if drone.next_zone().is_available():
                    if drone.link_opened(self.connections):
                        if (drone.next_zone().is_restricted()):
                            if not drone.is_flying:
                                drone.is_flying = True
                            else:
                                drone.is_flying = False
                                drone.step()
                        else:
                            drone.is_flying = False
                            drone.step()
            if all([ele.is_reached for ele in self.drones]):
                break
            self.reset_connection_link_capacity()
        print("Total turns: ", self.turnes)
