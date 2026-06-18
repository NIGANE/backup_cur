from typing import List
from src.models.Error import MyError
from src.models.Validator import Validator
from src.models.Manager import Manager
from src.models.Hub import Hub


class Parser():
    def __init__(self, argv: List[str]) -> None:
        self.argv = argv
        self.validator = Validator()
        self.manager = Manager()
        self.load_file()

    def load_file(self):
        data = []
        try:
            with open(self.argv[1], "r") as f:
                data = f.readlines()
            self.run_validation(data)
        except FileNotFoundError as e:
            raise MyError(f"FileNotFound {e}")

    def run_validation(self, data) -> None:
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
                self.manager.resolve_connection(connection, i + 1)
            else:
                raise MyError(
                    f"Error (): invalid configuration at line {i + 1}.")
