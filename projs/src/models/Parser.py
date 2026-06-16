from typing import List
from src.models.Error import MyError


class Parser():
    def __init__(self, argv: List[str]) -> None:
        self.argv = argv
        self.load_file()

    def load_file(self):
        data = []
        try:
            with open(self.argv[1], "r") as f:
                data = f.readlines()
            self.run_validation(data)
        except FileNotFoundError as e:
            raise MyError(f"FileNotFound {e}")

    def run_validation(self, data):
        for line in data:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if line.startswith("nb_drones"):
                self.validator.nb_drones(line)
            if line.startswith("start_hub") or line.startswith("end_hub") or line.startswith("hub"):
                self.validator.hubs(line)
            if line.startswith("connection"):
                self.validator.connection(line)
