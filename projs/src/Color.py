from enum import Enum
from typing import Optional


class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    BLACK = "black"
    YELLOW = "yellow"
    MAGENTA = "magenta"
    CYAN = "cyan"
    WHITE = "WHITE"

    @staticmethod
    def in_reserve(attr: str) -> Optional['Color']:
        for color in Color:
            if attr == color.value:
                return color
        return None
