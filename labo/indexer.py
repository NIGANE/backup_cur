from chunker import MinimalSource, Error
from typing import List, Tuple
from chunker import Chunker


class Indexer():
    def __init__(self, dest: str):
        self.chunks: List[Tuple[MinimalSource, str]] = Chunker.load(dest)

    def split(source: str):
        if not source:
            return []
        res: List[str] = []
        buffer: str = ''


        for i, char in enumerate(source):
            if char.isalnum():
                if char.isupper() and i > 0:
                    if (source[i - 1].islower()):
                        buffer.append(' ')
                        buffer.append(char.lower())
                else:
                    buffer.append(char.lower())
            else:
                buffer.append(' ')
                


