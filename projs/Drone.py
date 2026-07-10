from Hub import Hub
from typing import List, Optional
from Error import MyError
from Connection import Connection


class Drone:
    """Represent a drone participating in the simulation.

    A drone travels from its starting hub to its destination by following a
    precomputed path. It maintains its current position, traversal state,
    and any reserved hubs used during path planning.

    Attributes:
        name: The unique identifier of the drone.
        is_flying: Whether the drone is currently in transit.
        is_reached: Whether the drone has reached its destination.
        station: The hub currently occupied by the drone.
        path: The ordered sequence of hubs to traverse.
        index: The current position within the path.
        reserve: The hubs reserved for the drone during path planning.
    """
    def __init__(self, i: int, station: Hub):
        """Initialize a drone.

        Args:
            i: The drone identifier.
            station: The starting hub.
        """
        self.name: str = f"D{i}"
        self.is_flying: bool = False
        self.is_reached: bool = False
        self.station: Hub = station
        self.path: List[Hub] = []
        self.index: int = 0
        self.reserve: List[Hub] = []

    def set_path(self, path: List[Hub]) -> None:
        """Assign a traversal path to the drone.

        Args:
            path: The ordered sequence of hubs to traverse.
        """
        self.path = path
        path[0].append(self)

    def cur_zone(self) -> Hub:
        """Return the drone's current hub.

        Returns:
            The hub currently occupied by the drone.
        """
        return self.path[self.index]

    def next_zone(self) -> Hub:
        """Return the next hub in the drone's path.

        Returns:
            The next hub to visit.

        Raises:
            MyError: If no next hub exists.
        """
        if len(self.path) > self.index:
            return self.path[self.index + 1]
        raise MyError(
            f"Error: no solution path found for this drone [{self.name}]")

    def prev_zone(self) -> Hub:
        """Return the previous hub in the drone's path.

        Returns:
            The previously visited hub.

        Raises:
            MyError: If no previous hub exists.
        """
        if len(self.path) > self.index:
            return self.path[self.index - 1]
        raise MyError(
            f"Error: no solution path found for this drone [{self.name}]")

    def step(self) -> None:
        """Advance the drone to the next hub.

        The drone leaves its current hub, enters the next hub, updates its
        position within the path, and marks itself as reached if it arrives at
        its destination.
        """

        self.cur_zone().pop(self)
        self.next_zone().append(self)
        self.index += 1
        if self.cur_zone() == self.path[-1]:
            self.is_reached = True
        self.station = self.cur_zone()

    def link_opened(self, connections: List[Connection]) -> bool:
        """Determine whether the next connection can be traversed.

        If the connection has remaining capacity, its usage count is updated.

        Args:
            connections: The available connections in the simulation.

        Returns:
            ``True`` if the drone may traverse the connection; otherwise
            ``False``.
        """
        cur = self.cur_zone()
        next = self.next_zone()
        cur_connection: Optional[Connection] = Connection.get_connection(
            cur.name, next.name)
        if not cur_connection:
            raise MyError("Error: Connection not found")
        if cur_connection.max_lint == cur_connection.per_turn:
            return False
        cur_connection.per_turn += 1
        return True

    def __eq__(self, drone: object) -> bool:
        """Determine whether two drones are equal.

        Two drones are considered equal if they have the same identifier.

        Args:
            drone: The object to compare.

        Returns:
            ``True`` if both objects represent the same drone; otherwise
            ``False``.
        """
        if not isinstance(drone, Drone):
            return False
        if drone.name == self.name:
            return True
        return False

    def fly(self) -> None:
        cur_connection: Optional[Connection] = Connection.get_connection(
            self.next_zone().name, self.cur_zone().name)
        if not cur_connection:
            raise MyError("Error: connection not founded")
        if self.next_zone().is_restricted():
            if cur_connection.per_turn == cur_connection.max_lint:
                self.next_zone().reserved = True

            if (len(self.next_zone().deck)
                    + len(self.next_zone().in_reserve)
                    + 1) == self.next_zone().capacity:
                self.next_zone().reserved = True
        self.reserve.append(self.next_zone())
        self.next_zone().reserve(self)
        self.is_flying = True

    def fly_off(self) -> None:
        self.is_flying = False
        self.reserve.pop()
        self.next_zone().reserved = False
        if self in self.next_zone().in_reserve:
            self.next_zone().drop_reserve(self)

    def __str__(self) -> str:
        """Return a human-readable representation of the drone.

        Returns:
            A string containing the drone identifier and its current status.
        """
        return (
            f"{self.name} "
            f"[{'flying' if self.is_flying else 'in'}"
            f" {self.station.name}]")
