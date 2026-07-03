from typing import Optional, List, Dict, Any, TYPE_CHECKING
from enum import Enum
from src.Error import MyError
from src.Color import Color
import colorama
if TYPE_CHECKING:
    from src.Drone import Drone


class ZoneType(Enum):
    NORMAL = "normal"
    RESTRICTED = "restricted"
    PRIORITY = "priority"
    BLOCKED = "blocked"


class Hub:
    def __init__(self, x: int, y: int, name: str,
                 zone_type: ZoneType = ZoneType.NORMAL) -> None:
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

    def get_colored_name(self) -> str:
        if not self.color:
            return self.name
        return str(getattr(colorama.Fore, self.color) + self.name)

    def is_available(self) -> bool:
        if self.end:
            return True
        if (len(self.deck)) == self.capacity:
            return False
        return True

    def pop(self, drone: 'Drone') -> None:
        self.deck = [dro for dro in self.deck if dro != drone]

    def append(self, drone: 'Drone') -> None:
        if self.end:
            self.deck.append(drone)
            return
        if len(self.deck) == self.capacity:
            raise MyError(
                f"no space left to insert new drone into zone: {self.name}")
        self.deck.append(drone)

    def is_restricted(self) -> bool:
        return bool(self.type == ZoneType.RESTRICTED)

    def is_priority(self) -> bool:
        return self.type == ZoneType.PRIORITY

    def set_color(self, c: str) -> None:
        if c is None or c == "":
            return
        re: Optional[Color] = Color.in_reserve(c)
        if re:
            self.color = re.name

    def set_capacity(self, n: int) -> None:
        self.capacity = n

    def set_zone(self, zone: ZoneType) -> None:
        self.type = zone
        if self.type == ZoneType.RESTRICTED:
            self.cost = 2
        else:
            self.cost = 1

    def connect(self, hub: 'Hub', link_capacity: int) -> None:
        self.connections.append({"hub": hub, "link_capacity": link_capacity})

    def relax_hh(self, prev: 'Hub') -> None:
        self.relaxed = prev.relaxed + self.cost
        self.prev: 'Hub' = prev

    def relax_priority(self, prev: 'Hub') -> None:
        self.relaxed = -50
        self.prev = prev

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.x}, {self.y})"
            f"[color: {self.color}, capacity: {self.capacity}, "
            f"type: {self.type.value}]"
            " connections: ["
            f"{[ele["hub"].name for ele in self.connections]}"
            "]"
            )

    def __eq__(self, hub: object) -> bool:
        return (isinstance(hub, Hub)
                and self.x == hub.x and self.y == hub.y
                )
