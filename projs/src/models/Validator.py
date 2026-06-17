from typing import Optional, Tuple, Dict, List
from re import Match, Pattern, compile, search
from src.models.Error import MyError
from src.models.Hub import Hub
from src.models.Connection import Connection

class Validator():
    def __init__(self) -> None:
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
        match: Optional[Match] = search(self.nb, line)
        if not match:
            raise self.missmatch_error(i, "invalid configurations")
        nb: Optional[str] = match.groupdict().get("count")
        if (not nb
                or not self.is_number(nb)
                or int(nb) < 0):
            raise self.missmatch_error(i, "invalid number")
        return int(nb)

    def hubs(self, line: str, i: int) -> Hub:
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
        if groups.get("config"):
            config: List[str] = groups["config"].strip().split()
            for conf in config:
                if conf.startswith("color"):
                    if self.valid_color(conf.split("=")[1]):
                        hub.set_color(conf.split("=")[1])
                    else:
                        raise self.missmatch_error(i, "invalid color")
                if conf.startswith("max_drones"):
                    if self.is_number(conf.split("=")[1]):
                        size: int = int(conf.split("=")[1])
                        hub.set_capacity(size)
        if line.startswith("start_hub"):
            hub.start = True
        if line.startswith("end_hub"):
            hub.end = True
        return hub

    def connections(self, line: str, i: int) -> Connection:
        match: Optional[Match] = search(self.con_pattern, line)
        if not match:
            raise self.missmatch_error(i, "invalid configurations")
        groups: Dict[str, str] = match.groupdict()
        max_lint: int = 1
        conf: Optional[str] = groups.get("config")
        if conf:
            if self.is_number(conf.strip().split("=")[1]):
                max_lint = int(conf.strip().split("=")[1])
            else:
                raise self.missmatch_error(i, "invalid number")
        connection = Connection(groups["hub1"], groups["hub2"], max_lint)
        return connection

    def is_number(self, n: Optional[str]) -> bool:
        if not n:
            return False
        patt = compile(r"^\-?\d+$")
        match = search(patt, n)
        return bool(match)

    @staticmethod
    def missmatch_error(line: int, desc: Optional[str] = "") -> MyError:
        return MyError(f"mismatch configuration at line: {line} ({desc})")

    def valid_color(self, s: str) -> bool:
        if not s:
            return False
        patt = compile(r"^[a-zA-z]+$")
        return bool(search(patt, s))
