from typing import Any, List
from Drone import Drone
from Hub import Hub


class Tools:
    """Provide utility functions used throughout the simulation.

    This class groups helper methods for working with collections and
    displaying simulation state.
    """
    @staticmethod
    def indexof(ele: Any, seq: List[Any]) -> int:
        """Return the index of an element in a sequence.

        Args:
            ele: The element to locate.
            seq: The sequence to search.

        Returns:
            The index of the first occurrence of ``ele`` if found;
            otherwise ``-1``.
        """
        i: int = 0
        while i < len(seq):
            if seq[i] == ele:
                return i
            i += 1
        return -1

    @staticmethod
    def fetch_drones(drones: List[Drone]) -> None:
        """Print the current state of each drone.

        Args:
            drones: The drones to display.
        """
        for dr in drones:
            print(
                f"- {dr.name} [{dr.cur_zone().name}]"
                f"{' => Fly-in' if dr.is_flying else ''}")

    @staticmethod
    def fetch_paths(paths: List[List[Hub]]) -> None:
        """Print the discovered paths.

        Each path is displayed as an ordered sequence of hub names along
        with their capacities.

        Args:
            paths: The paths to display.
        """
        for path in paths:
            for zone in path:
                print("*", zone.name, f"({zone.capacity})", end=" ")
            print("\n")
