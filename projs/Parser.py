from typing import List
from Error import MyError
from Validator import Validator
from Manager import Manager
from Hub import Hub


class Parser():
    """Parse and validate a simulation configuration file.

    This class loads the configuration file, delegates validation to a
    ``Validator``, and builds a ``Manager`` instance containing the
    validated simulation state.
    """
    def __init__(self, argv: List[str]) -> None:
        """Initialize the parser.

        Args:
            argv: The command-line arguments.
        """
        self.argv = argv
        self.validator = Validator()
        self.manager = Manager()

    def load_file(self) -> List[str]:
        """Load the configuration file.

        Returns:
            The lines read from the configuration file.

        Raises:
            MyError: If the configuration file cannot be found.
        """
        data = []
        try:
            with open(self.argv[1], "r") as f:
                data = f.readlines()
            return data
        except FileNotFoundError as e:
            raise MyError(f"FileNotFound {e}")

    def run_validation(self, data: List[str]) -> Manager:
        """Validate the configuration and construct the simulation manager.

        The configuration is processed line by line. Each directive is
        validated
        and used to populate the simulation manager with drones, hubs, and
        connections.

        Args:
            data: The configuration file contents.

        Returns:
            A fully initialized ``Manager`` instance.

        Raises:
            MyError: If the configuration contains invalid syntax, duplicate
                entities, missing required data, or inconsistent definitions.
        """
        for i, line in enumerate(data):
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if line.startswith("nb_drones"):
                count: int = self.validator.nb_drones(line, i + 1)
                self.manager.set_total_drones(count)

            elif (line.startswith("start_hub") or line.startswith("end_hub")
                    or line.startswith("hub")):
                hub: Hub = self.validator.hubs(line, i + 1)
                self.manager.add_hub(hub, i + 1)

            elif line.startswith("connection"):
                connection = self.validator.connections(line, i + 1)
                for con in self.manager.connections:
                    if connection == con:
                        raise self.validator.missmatch_error(
                            i + 1, "Duplicate connection")
                self.manager.resolve_connection(connection, i + 1)
            else:
                raise MyError(
                    "Error (invalid configurations): "
                    f"invalid configuration at line {i + 1}.")
        self.manager.set_endpoints()
        if len(self.manager.hubs) < 1:
            raise MyError("Error (configuration error): 0 provided hubs")
        if self.manager.total_drones < 1:
            raise MyError("Error (configuration error): 0 provided drones")
        return self.manager
