

class Connection:
    def __init__(self, hub1: str, hub2: str, max_lint: int = 1):
        self.hub1: str = hub1
        self.hub2: str = hub2
        self.max_lint: int = max_lint

    def __str__(self):
        return (f"connection: {self.hub1} - {self.hub2} :: "
                f"capacity: {self.max_lint}")
