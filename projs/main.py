from Errors import *
from dotenv import load_dotenv
import os
load_dotenv()

min_required_width = int(os.getenv("min_required_width"))
min_required_height = int(os.getenv("min_required_height"))


class MazeGen:

    def __init__(self, wd, he) -> None:
        self.wd = wd
        self.he = he
        self.init_val = 15
        if self.wd < min_required_width or self.he < min_required_height:
            raise CoordinatesError("error of cordinates")
        self.arr = [[15 for _ in range(self.wd)]for _ in range(self.he)]

    def get_rep(self):
        # print("[")
        for r in self.arr:
            for c in r:
                print(c, end=" ")
            print("")


new_maze = MazeGen(7, 7)
new_maze.get_rep()
