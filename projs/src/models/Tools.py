from typing import Any, List


class Tools:
    @staticmethod
    def indexof(ele: Any, seq: List[Any]) -> int:
        i: int = 0
        while i < len(seq):
            if seq[i] == ele:
                return i
            i += 1
        return -1
