from typing import List, Optional
from Hub import Hub, ZoneType
from Connection import Connection
from Error import MyError
from Drone import Drone
import colorama

colorama.init(autoreset=True)


class Manager:
    """Manage the simulation lifecycle.

    This class stores the simulation state, computes valid paths between the
    start and destination hubs, distributes drones across those paths, and
    executes the simulation turn by turn.

    Attributes:
        total_drones: The number of drones in the simulation.
        hubs: The hubs forming the navigation graph.
        shortest_path: The shortest path from the start to the destination.
        paths: The candidate paths available for routing drones.
        drones: The drones participating in the simulation.
        turnes: The number of simulation turns elapsed.
        running_sim: Whether the simulation is currently running.
        connections: The graph connections between hubs.
        tracked_drones: The drones whose movements are displayed each turn.
    """
    def __init__(self) -> None:
        """Initialize an empty simulation manager."""
        self.total_drones: int = 0
        self.hubs: List[Hub] = []
        self.shortest_path: List[Hub] = []
        self.paths: List[List[Hub]] = []
        self.drones: List[Drone] = []
        self.turnes: int = 0
        self.running_sim: bool = False
        self.connections: List[Connection] = []
        self.tracked_drones: List[Drone] = []

    def set_endpoints(self) -> None:
        """Locate the start and destination hubs.

        Raises:
            MyError: If the start or destination hub cannot be found.
        """
        try:
            self.start: Hub = [ele for ele in self.hubs if ele.start][0]
            self.end: Hub = [ele for ele in self.hubs if ele.end][0]
        except Exception:
            raise MyError("Error: no start/end hub founded")

    def get_total_cost(self, path: List[Hub]) -> float:
        """Compute the traversal cost of a path.

        Args:
            path: The path to evaluate.

        Returns:
            The total traversal cost.
        """
        total: float = 0
        for ele in path:
            total += ele.cost
        return total

    def set_total_drones(self, nb: int) -> None:
        """Set the number of drones.

        Args:
            nb: The total number of drones.
        """
        self.total_drones = nb

    def add_hub(self, hub: Hub, line: int) -> None:
        """Add a hub to the simulation.

        Args:
            hub: The hub to add.
            line: The configuration file line where the hub was defined.

        Raises:
            MyError: If the hub is duplicated or multiple start or destination
                hubs are defined.
        """
        for ele in self.hubs:
            if ele == hub or ele.name == hub.name:
                raise MyError(
                    "Error (Invalid configuraions): duplicate hub"
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
        """Compute the minimum traversal cost to every reachable hub.

        Raises:
            MyError: If no path exists from the start to the destination.
        """
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
                    if target.is_priority():
                        target.relax_priority(cur)
                    else:
                        target.relax_hh(cur)
        if self.end.relaxed == float("inf"):
            raise MyError("Error: No solution path founded")

    def path_finding(self) -> None:
        """Compute and filter the candidate paths for the simulation."""
        self.relaxation()
        self.find_shortest_path()
        self.discover_multiple_paths()
        self.paths_filter_by_cost(
            self.get_total_cost(self.shortest_path) * 1.38)
        if (len(self.paths) > 4):
            self.paths_filter_by_len(len(self.shortest_path) + 2)

    def paths_filter_by_cost(self, min_cost: float) -> None:
        """Discard paths whose cost exceeds the given threshold.

        Args:
            min_cost: The maximum allowed traversal cost.
        """
        new_list: List[List[Hub]] = []
        for path in self.paths:
            co: float = self.get_total_cost(path)
            if min_cost > co:
                new_list.append(path)
        self.paths = new_list

    def paths_filter_by_len(self, min_len: int) -> None:
        """Discard paths longer than the given length.

        Args:
            min_len: The maximum allowed path length.
        """
        new_list: List[List[Hub]] = []
        for path in self.paths:
            if len(path) <= min_len:
                new_list.append(path)
        self.paths = new_list

    def find_shortest_path(self) -> None:
        """Reconstruct the shortest path from the relaxation results."""
        cur: Hub = self.end
        while (True):
            self.shortest_path = [cur, *self.shortest_path]
            if cur == self.start:
                break
            cur = cur.prev

    def discover_multiple_paths(self) -> None:
        """Discover alternative paths between the endpoints."""
        new_path: Optional[List[Hub]] = self.shortest_path
        while new_path is not None:
            if new_path in self.paths:
                break
            for ele in new_path:
                ele.relaxed += 100.0
            self.paths.append(new_path)
            new_path = self.resolve_new_path()

    def resolve_new_path(self) -> Optional[List[Hub]]:
        """Construct an alternative path.

        Returns:
            An alternative path if one exists; otherwise ``None``.
        """
        self.unvisit()
        stack: List[Hub] = [self.start]
        cur: Hub = stack[-1]
        while (cur != self.end):
            cur.visited = True
            target: Optional[Hub] = self.get_chepest(cur)
            if (target and target.type == ZoneType.BLOCKED):
                return None
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
        """Return the cheapest reachable neighboring hub.

        Priority hubs are preferred over cost-based selection.

        Args:
            hub: The current hub.

        Returns:
            The selected neighboring hub, or ``None`` if none is available.
        """
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

    def resolve_connection(self, con: Connection, line: int) -> None:
        """Validate and register a connection.

        Args:
            con: The connection to register.
            line: The configuration file line where the connection was defined.

        Raises:
            MyError: If the connection references unknown hubs or the required
                endpoints are missing.
        """
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
        """Return the hub with the given name.

        Args:
            name: The hub identifier.

        Returns:
            The matching hub, or ``None`` if it does not exist.
        """
        for ele in self.hubs:
            if ele.name == name:
                return ele
        return None

    def any_priority(self, hubs: List[Hub]) -> Optional[Hub]:
        """Return the first priority hub.

        Args:
            hubs: The hubs to inspect.

        Returns:
            The first priority hub, or ``None`` if none exists.
        """
        for ele in hubs:
            if ele.type == ZoneType.PRIORITY.value:
                return ele
        return None

    def unvisit(self) -> None:
        """Clear the visited state of every hub."""
        for hub in self.hubs:
            hub.visited = False

    def __str__(self) -> str:
        """Return a human-readable summary of the simulation manager.

        Returns:
            A string containing the total number of hubs and drones managed by
            the simulation.
        """
        return (f"hubs: {len(self.hubs)} "
                f"total drones: {self.total_drones}"
                )

    def split_drones(self) -> None:
        """Distribute drones across the available paths."""
        for ind, ele in enumerate(self.drones):
            ele.set_path(self.paths[(ind + 1) % len(self.paths)])

    def reset_connection_link_capacity(self) -> None:
        """Reset the per-turn usage of every connection.

        Clears the number of traversals recorded for each connection during the
        current simulation turn, allowing all connections to be reused in the
        next turn.
        """
        for con in self.connections:
            con.per_turn = 0

    def run_simulation(self) -> None:
        """Execute the drone simulation.

        Drones are created, assigned paths, and advanced turn by turn until all
        of them reach the destination.
        """
        i: int = 0
        self.running_sim = True
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
                if drone.next_zone() in drone.reserve:
                    drone.fly_off()
                    self.tracked_drones.append(drone)
                    drone.step()
                elif drone.next_zone().is_available():
                    if drone.link_opened():
                        if (drone.next_zone().is_restricted()):
                            if (not drone.is_flying):
                                drone.fly()
                                self.tracked_drones.append(drone)
                        else:
                            drone.is_flying = False
                            self.tracked_drones.append(drone)
                            drone.step()
            self.tracking_output()
            if all([ele.is_reached for ele in self.drones]):
                break
            self.reset_connection_link_capacity()
        print("Total turns: ", self.turnes)

    def tracking_output(self) -> None:
        """Print the drones that moved during the current simulation turn."""
        i = len(self.tracked_drones) - 1
        for ele in self.tracked_drones:
            print(f"{ele.name}", end="-")
            if ele.is_flying:
                print(
                    f"{ele.cur_zone().get_colored_name()}",
                    f"-{ele.next_zone().get_colored_name()}",
                    end="", sep="")
            else:
                print(f"{ele.cur_zone().get_colored_name()}", end="")
            if i != 0:
                print(", ", end="")
            i -= 1
        print("")
        self.tracked_drones = []
