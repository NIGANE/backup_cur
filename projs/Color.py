from enum import Enum
from typing import Optional
from colorama import Fore


class Colorama(Enum):
    """Enumerate the colors to use them on output.

    These values represent the valid colors that may be
    used to color the hubs names.
    """
    RED = Fore.RED
    GREEN = Fore.GREEN
    BLUE = Fore.BLUE
    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    BLACK = Fore.BLACK

    BROWN = "\033[38;2;139;69;19m"
    PURPLE = "\033[38;2;128;0;128m"
    ORANGE = "\033[38;2;255;165;0m"
    MAGENTA = "\033[38;2;255;0;255m"
    LIME = "\033[38;2;50;205;50m"
    MAROON = "\033[38;2;128;0;0m"
    GOLD = "\033[38;2;255;215;0m"
    DARKRED = "\033[38;2;139;0;0m"
    CRIMSON = "\033[38;2;220;20;60m"
    VIOLET = "\033[38;2;148;0;211m"


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
    WHITE = "white"
    ORANGE = "orange"
    BROWN = "brown"
    PURPLE = "purple"
    LIME = "lime"
    MAROON = "maroon"
    GOLD = "gold"
    DARKRED = "darkred"
    CRIMSON = "crimson"
    VIOLET = "violet"

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
