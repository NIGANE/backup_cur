from typing import Optional, List, Dict, Any
from enum import Enum
from src.Dron import Drone


class ZoneType(Enum):
    NORMAL = "normal"
    RESTRICTED = "restricted"
    PRIORITY = "priority"
    BLOCKED = "blocked"


class Hub:
    def __init__(self, x, y, name: str,
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
        self.deck: List[Drone] = []

    def is_available(self) -> bool:
        if (self.deck) == self.capacity:
            return False
        return True

    def is_restricted(self) -> bool:
        return bool(self.type == ZoneType.RESTRICTED)

    def set_color(self, c: str) -> None:
        self.color = c

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

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.x}, {self.y})"
            f"[color: {self.color}, capacity: {self.capacity}, "
            f"type: {self.type.value}]"
            f"{"-> start" if self.start else ""}"
            f"{"-> end" if self.end else ""} "
            "connections: \n["
            f"{[ele["hub"].name for ele in self.connections]}"
            "]"
            )

    def __eq__(self, hub: object):
        if not isinstance(hub, Hub):
            return False
        if self.x == hub.x and self.y == hub.y:
            return True
        return False
