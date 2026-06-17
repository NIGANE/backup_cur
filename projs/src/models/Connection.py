

class Connection:
    def __init__(self, hub1: str, hub2: str, max_lint: int = 1):
        self.hub1: str = hub1
        self.hub2: str = hub2
        self.max_lint: int = max_lint
