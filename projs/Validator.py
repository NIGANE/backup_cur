from typing import Optional, Tuple, Dict, List
from re import Match, Pattern, compile, search
from Error import MyError
from Hub import Hub, ZoneType
from Connection import Connection


class Validator():
    """Validate simulation configuration directives.

    This class parses and validates the directives found in a simulation
    configuration file. It converts validated input into domain objects such
    as ``Hub`` and ``Connection`` while ensuring that configuration values
    satisfy the expected constraints.
    """
    def __init__(self) -> None:
        """Initialize the validator.

        Compiles the regular expressions used to validate configuration
        directives.
        """
        self.hub_pattern: Pattern = compile(
            r"^\w+:\s(?P<name>\w+)\s(?P<x>(\-?\d+))\s(?P<y>(\-?\d+))"
            r"(?:\s\[(?P<config>\w+=\w+(?:\s\w+=\w+)*)\])?$")
        self.con_pattern: Pattern = compile(
            r"^connection:\s(?P<hub1>([a-zA-z0-9-_]+))\-"
            r"(?P<hub2>([a-zA-z0-9-_]+))"
            r"(?:\s\[(?P<config>\w+=\w+)\])?$")
        self.nb: Pattern = compile(
            r"^nb_drones:\s(?P<count>\d+)$")

    def nb_drones(self, line: str, i: int) -> int:
        """Validate the drone count directive.

        Args:
            line: The configuration line.
            i: The line number.

        Returns:
            The validated number of drones.

        Raises:
            MyError: If the directive is malformed or contains an invalid drone
                count.
        """
        match: Optional[Match] = search(self.nb, line)
        if not match:
            raise self.missmatch_error(i, "invalid configurations")
        nb: Optional[str] = match.groupdict().get("count")
        if (not nb
                or not self.is_number(nb)
                or int(nb) < 0):
            raise self.missmatch_error(i, "invalid number")
        self.drones_count: int = int(nb)
        return int(nb)

    def hubs(self, line: str, i: int) -> Hub:
        """Validate a hub definition.

        Parses the hub definition, validates its attributes, and constructs the
        corresponding ``Hub`` object.

        Args:
            line: The configuration line.
            i: The line number.

        Returns:
            The validated hub.

        Raises:
            MyError: If the hub definition is invalid or contains unsupported
                configuration options.
        """
        if 'drones_count' not in self.__dict__:
            raise MyError(
                "Error: nb_drones must be "
                "provided at the top of the config file")
        match: Optional[Match] = search(self.hub_pattern, line)
        if not match:
            raise self.missmatch_error(i, "invalid configuration")

        groups: Dict[str, str] = match.groupdict()
        if not (groups.get("name")):
            raise self.missmatch_error(i, "invalid name for hub")

        hub_name: str = groups["name"]
        coordinates: Tuple[Optional[str], Optional[str]] = (
            groups.get("x"), groups.get("y"))
        if not (all([self.is_number(ele) for ele in coordinates])):
            raise self.missmatch_error(i, "invalid number")

        hub = Hub(int(groups["x"]), int(groups["y"]), hub_name)

        if line.startswith("start_hub"):
            hub.start = True
        if line.startswith("end_hub"):
            hub.end = True

        if groups.get("config"):
            config: List[str] = groups["config"].strip().split()
            allowed = ["color", "max_drones", "zone"]
            if not all([param.strip().split("=")[0]
                        in allowed for param in config]):
                raise self.missmatch_error(i, "invalid Hub configuration")
            for conf in config:
                if conf.startswith("color"):
                    if self.valid_color(conf.split("=")[1]):
                        hub.set_color(conf.split("=")[1])
                    else:
                        raise self.missmatch_error(i, "invalid color")
                if conf.startswith("max_drones"):
                    if self.is_number(conf.split("=")[1]):
                        size: int = int(conf.split("=")[1])
                        if size == 0 and not (hub.start or hub.end):
                            raise self.missmatch_error(
                                i, "invalid zone capacity")
                        hub.set_capacity(size)
                else:
                    if (line.startswith("start_hub")
                            or line.startswith("end_hub")):
                        hub.capacity = self.drones_count
                if conf.startswith("zone"):
                    zone: Optional[ZoneType] = self.is_valid_zone(
                        conf.split("=")[1].strip())
                    if zone:
                        hub.set_zone(zone)
                    else:
                        raise self.missmatch_error(i, "invalid zone type")
        return hub

    def connections(self, line: str, i: int) -> Connection:
        """Validate a connection definition.

        Args:
            line: The configuration line.
            i: The line number.

        Returns:
            The validated connection.

        Raises:
            MyError: If the connection definition is malformed or contains an
                invalid configuration.
        """
        match: Optional[Match] = search(self.con_pattern, line)
        if not match:
            raise self.missmatch_error(i, "invalid configurations")
        groups: Dict[str, str] = match.groupdict()
        link_capacity: int = 1
        conf: Optional[str] = groups.get("config")
        if conf:
            if conf.strip().split("=")[0] not in ["max_link_capacity"]:
                raise self.missmatch_error(i, "invalid link configuration")
            if self.is_number(conf.strip().split("=")[1]):
                link_capacity = int(conf.strip().split("=")[1])
                if link_capacity == 0:
                    raise self.missmatch_error(
                        i, "invalid connection capacity")
            else:
                raise self.missmatch_error(i, "invalid number")
        connection = Connection(groups["hub1"], groups["hub2"], link_capacity)
        return connection

    def is_number(self, n: Optional[str]) -> bool:
        """Determine whether a string represents an integer.

        Args:
            n: The string to validate.

        Returns:
            ``True`` if the string represents a signed integer; otherwise
            ``False``.
        """
        if not n:
            return False
        patt = compile(r"^\-?\d+$")
        match = search(patt, n)
        return bool(match)

    def is_valid_zone(self, zone: str) -> Optional[ZoneType]:
        """Return the matching zone type.

        Args:
            zone: The zone name.

        Returns:
            The corresponding ``ZoneType`` if the zone is supported;
            otherwise ``None``.
        """
        for ele in ZoneType:
            if ele.value == zone:
                return ele
        return None

    @staticmethod
    def missmatch_error(line: int, desc: Optional[str] = "") -> MyError:
        """Create a configuration mismatch error.

        Args:
            line: The line where the error occurred.
            desc: A description of the validation failure.

        Returns:
            A ``MyError`` describing the configuration mismatch.
        """
        return MyError(f"mismatch configuration at line: {line} ({desc})")

    def valid_color(self, s: str) -> bool:
        """Determine whether a color name is valid.

        Args:
            s: The color name.

        Returns:
            ``True`` if the color name consists only of alphabetic characters;
            otherwise ``False``.
        """
        if not s:
            return False
        patt = compile(r"^[a-zA-z]+$")
        return bool(search(patt, s))
