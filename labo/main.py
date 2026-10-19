from chunker import Chunker
from indexer import Indexer


def main():
    max_size = 2000
    chunker = Chunker("test", "data/process")
    cnk_path = chunker.discover_files().chunk()
    indexer = Indexer("data/process")
    idx_path = indexer.tokenize_chunks(str(cnk_path))
    loads = indexer.load(str(idx_path))

main()
