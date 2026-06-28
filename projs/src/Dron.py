from src.models.Hub import Hub


class Dron:
    def __init__(self, i: int, station: Hub):
        self.name: str = f"D{i}"
        self.is_flying: bool = False
        self.is_reached: bool = False
        self.station: Hub = station
