

class Connection:
    def __init__(self, hub1: str, hub2: str, max_lint: int = 1):
        self.hub1: str = hub1
        self.hub2: str = hub2
        self.max_lint: int = max_lint
        self.per_turn: int = 0

    def __str__(self) -> str:
        return (f"connection: {self.hub1} - {self.hub2} :: "
                f"capacity: {self.max_lint}")

    def __eq__(self, con: object) -> bool:
        return (isinstance(con, Connection)
                and ((self.hub1 == con.hub1 and self.hub2 == con.hub2)
                or (self.hub1 == con.hub2 and self.hub2 == con.hub1)))

    def __hash__(self) -> int:
        return hash(f"{self.hub1}-{self.hub2}")
