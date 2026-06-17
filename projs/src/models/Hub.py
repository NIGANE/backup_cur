from typing import Optional, List, Dict, Any


class Hub:
    def __init__(self, x, y, name: str) -> None:
        self.x: int = x
        self.y: int = y
        self.name: str = name
        self.color: Optional[str] = None
        self.capacity: int = 1
        self.start: bool = False
        self.end: bool = False
        self.connections: List[Dict[str, Any]] = []

    def set_color(self, c: str) -> None:
        self.color = c

    def set_capacity(self, n: int) -> None:
        self.capacity = n

    def connect(self, hub: 'Hub', max_lint: int) -> None:
        self.connections.append({"hub": hub, "max_lint": max_lint})

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.x}, {self.y})"
            f"[color: {self.color}, capacity: {self.capacity}]"
            f"{"-> start" if self.start else ""}"
            f"{"-> end" if self.end else ""}"
            )

    def __eq__(self, hub: object):
        if not isinstance(hub, Hub):
            return False
        if self.x == hub.x and self.y == hub.y:
            return True
        return False
