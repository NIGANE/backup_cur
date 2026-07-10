from typing import List, Optional


class Connection:
    """Represent a bidirectional connection between two hubs.

    A connection links two hubs and tracks the maximum number of entities
    that may traverse it during a simulation turn.

    Attributes:
        hub1: The name of the first hub.
        hub2: The name of the second hub.
        max_lint: The maximum number of entities allowed to use the
            connection per turn.
        per_turn: The number of entities that have used the connection in
            the current simulation turn.
    """
    connections: List['Connection'] = []

    @classmethod
    def get_connection(cls, hub1: str, hub2: str) -> Optional['Connection']:
        for con in cls.connections:
            if ((con.hub1 == hub1 and con.hub2 == hub2)
                    or (con.hub2 == hub1 and con.hub1 == hub2)):
                return con
        return None

    @classmethod
    def new_connection(cls, con: 'Connection') -> None:
        cls.connections.append(con)

    def __init__(self, hub1: str, hub2: str, max_lint: int = 1):
        """Initialize a connection.

        Args:
            hub1: The name of the first hub.
            hub2: The name of the second hub.
            max_lint: The maximum number of entities allowed to traverse the
                connection per simulation turn. Defaults to ``1``.
        """
        self.hub1: str = hub1
        self.hub2: str = hub2
        self.max_lint: int = max_lint
        self.per_turn: int = 0
        self.new_connection(self)

    def __str__(self) -> str:
        """Return a human-readable representation of the connection.

        Returns:
            A string describing the connected hubs and the connection
            capacity.
        """
        return (f"connection: {self.hub1} - {self.hub2} :: "
                f"capacity: {self.max_lint}")

    def __eq__(self, con: object) -> bool:
        """Determine whether two connections are equivalent.

        Two connections are considered equal if they connect the same pair
        of hubs, regardless of their order.

        Args:
            con: The object to compare with this connection.

        Returns:
            ``True`` if both connections link the same hubs; otherwise
            ``False``.
        """
        return (isinstance(con, Connection)
                and ((self.hub1 == con.hub1 and self.hub2 == con.hub2)
                or (self.hub1 == con.hub2 and self.hub2 == con.hub1)))

    def __hash__(self) -> int:
        """Return the hash of the connection.

        Returns:
            A hash value derived from the connected hubs.
        """
        return hash(tuple(sorted((self.hub1, self.hub2))))
