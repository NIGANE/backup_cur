from chunker import Chunker
from indexer import Indexer


def main():
    max_size = 2000
    chunker = Chunker("test", "data/process")
    chunker.discover_files().chunk()
    str(chunker)
    chunker.save()
    indexer = Indexer(chunker.dest)


main()
