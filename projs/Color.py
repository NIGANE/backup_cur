from enum import Enum
from typing import Optional


class Color(Enum):
    """Enumerate the colors supported by the simulation.

    These values represent the valid colors that may be assigned to
    entities during parsing and validation.
    """
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
        """Return the matching color enumeration.

        Args:
            attr: The color name to look up.

        Returns:
            The corresponding ``Color`` member if ``attr`` is a supported
            color; otherwise ``None``.
        """
        for color in Color:
            if attr == color.value:
                return color
        return None
