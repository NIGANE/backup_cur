from chunker import Chunker
from indexer import Indexer


def main():
    max_size = 2000
    chunker = Chunker("test", "data/process")
    chunker.discover_files().chunk()
    str(chunker)
    chunker.save()
    indexer = Indexer()
    tokens = indexer.tokenize_chunks(chunker.dest)
    term_freq = indexer.term_frequency(tokens)
    doc_freq = indexer.doc_frequency(tokens)
    lenth = indexer.lenth(tokens)
    idf = indexer.idf(doc_freq, len(tokens))
    print(idf)


main()
