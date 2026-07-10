from typing import Optional, List, Dict, Any, TYPE_CHECKING
from enum import Enum
from Error import MyError
from Color import Color
import colorama
if TYPE_CHECKING:
    from Drone import Drone


class ZoneType(Enum):
    """Enumerate the supported zone types.

    These values define the traversal behavior and cost associated with a
    hub during path planning and simulation.
    """
    NORMAL = "normal"
    RESTRICTED = "restricted"
    PRIORITY = "priority"
    BLOCKED = "blocked"


class Hub:
    """Represent a hub in the simulation graph.

    A hub stores its position, traversal properties, connections to adjacent
    hubs, and the drones currently occupying it. It also maintains state
    used during path-finding algorithms.

    Attributes:
        x: The x-coordinate of the hub.
        y: The y-coordinate of the hub.
        name: The unique hub identifier.
        type: The zone type of the hub.
        color: The display color of the hub.
        capacity: The maximum number of drones allowed in the hub.
        start: Whether the hub is a starting location.
        end: Whether the hub is a destination.
        connections: The neighboring hubs and their link capacities.
        visited: Whether the hub has been visited during path finding.
        relaxed: The current shortest-path cost.
        cost: The traversal cost of entering the hub.
        reserved: Whether the hub is reserved.
        deck: The drones currently occupying the hub.
    """
    def __init__(self, x: int, y: int, name: str,
                 zone_type: ZoneType = ZoneType.NORMAL) -> None:
        """Initialize a hub.

        Args:
            x: The x-coordinate.
            y: The y-coordinate.
            name: The hub identifier.
            zone_type: The type of the hub. Defaults to
                ``ZoneType.NORMAL``.
        """
        self.x: int = x
        self.y: int = y
        self.name: str = name
        self.type: ZoneType = zone_type
        self.color: Optional[str] = None
        self.capacity: int = 1
        self.start: bool = False
        self.end: bool = False
        self.connections: List[Dict[str, Any]] = []
        self.visited: bool = False
        self.relaxed: float = float("+inf")
        self.cost: float = 2 if self.type == ZoneType.RESTRICTED else 1
        self.deck: List['Drone'] = []
        self.in_reserve: List['Drone'] = []

    def reserve(self, drone: 'Drone') -> None:
        """Reserve this hub for a drone.

        Adds the drone to the list of drones that have reserved the hub.

        Args:
            drone: The drone reserving the hub.
        """
        self.in_reserve.append(drone)

    def drop_reserve(self, drone: 'Drone') -> None:
        """Remove a drone's reservation from the hub.

        Args:
            drone: The drone whose reservation should be removed.
        """
        i: int = 0
        for drn in self.in_reserve:
            if drn == drone:
                self.in_reserve.pop(i)
            i += 1

    def get_colored_name(self) -> str:
        """Return the hub name with terminal color formatting.

        Returns:
            The colored hub name if a color is assigned; otherwise the plain
            hub name.
        """
        if not self.color:
            return self.name
        return str(getattr(colorama.Fore, self.color) + self.name)

    def is_available(self) -> bool:
        """Determine whether the hub can accept another drone.

        Destination hubs are always considered available.

        Returns:
            ``True`` if the hub has remaining capacity or is a destination;
            otherwise ``False``.
        """
        if self.end:
            return True
        if (len(self.deck) + len(self.in_reserve)) == self.capacity:
            return False
        return True

    def pop(self, drone: 'Drone') -> None:
        """Remove a drone from the hub.

        Args:
            drone: The drone to remove.
        """
        self.deck = [dro for dro in self.deck if dro != drone]

    def append(self, drone: 'Drone') -> None:
        """Add a drone to the hub.

        Args:
            drone: The drone to add.

        Raises:
            MyError: If the hub has reached its capacity.
        """
        if self.end or self.start:
            self.deck.append(drone)
            return
        if len(self.deck) == self.capacity:
            raise MyError(
                f"no space left to insert new drone into zone: {self.name}")
        self.deck.append(drone)

    def is_restricted(self) -> bool:
        """Determine whether the hub is a restricted zone.

        Returns:
            ``True`` if the hub is restricted; otherwise ``False``.
        """
        return bool(self.type == ZoneType.RESTRICTED)

    def is_priority(self) -> bool:
        """Determine whether the hub is a priority zone.

        Returns:
            ``True`` if the hub is a priority zone; otherwise ``False``.
        """
        return self.type == ZoneType.PRIORITY

    def set_color(self, c: str) -> None:
        """Assign a display color to the hub.

        Args:
            c: The color name.
        """
        if c is None or c == "":
            return
        re: Optional[Color] = Color.in_reserve(c)
        if re:
            self.color = re.name

    def set_capacity(self, n: int) -> None:
        """Set the hub capacity.

        Args:
            n: The maximum number of drones the hub can hold.
        """
        self.capacity = n

    def set_zone(self, zone: ZoneType) -> None:
        """Set the hub's zone type.

        Updates the traversal cost to match the selected zone type.

        Args:
            zone: The new zone type.
        """
        if (zone == ZoneType.BLOCKED and self.start or self.end):
            raise MyError("Error: no solution path would be "
                          "founded if start/end zones are blocked")
        self.type = zone
        if self.type == ZoneType.RESTRICTED:
            self.cost = 2
        else:
            self.cost = 1

    def connect(self, hub: 'Hub', link_capacity: int) -> None:
        """Connect this hub to another hub.

        Args:
            hub: The neighboring hub.
            link_capacity: The maximum number of drones allowed to traverse the
                connection per simulation turn.
        """
        self.connections.append({"hub": hub, "link_capacity": link_capacity})

    def relax_hh(self, prev: 'Hub') -> None:
        """Relax the hub during shortest-path computation.

        Args:
            prev: The predecessor hub in the current shortest path.
        """
        self.relaxed = prev.relaxed + self.cost
        self.prev: 'Hub' = prev

    def relax_priority(self, prev: 'Hub') -> None:
        """Relax the hub as a priority zone.

        Priority hubs are assigned a highly favorable cost to encourage their
        selection during path finding.

        Args:
            prev: The predecessor hub in the current shortest path.
        """
        self.relaxed = 0
        self.prev = prev

    def __str__(self) -> str:
        """Return a human-readable representation of the hub.

        Returns:
            A string describing the hub and its connections.
        """
        return (
            f"{self.name} ({self.x}, {self.y})"
            f"[color: {self.color}, capacity: {self.capacity}, "
            f"type: {self.type.value}]"
            " connections: ["
            f"{[ele['hub'].name for ele in self.connections]}"
            "]"
            )

    def __eq__(self, hub: object) -> bool:
        """Determine whether two hubs are equal.

        Two hubs are considered equal if they occupy the same coordinates.

        Args:
            hub: The object to compare.

        Returns:
            ``True`` if both hubs have the same coordinates; otherwise
            ``False``.
        """
        return (isinstance(hub, Hub)
                and self.x == hub.x and self.y == hub.y
                )
