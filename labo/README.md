## BUGS:
 - bug on Indexer [split]
    ### test:
    "HELLOworld" -> "helloworld" ("hello", "world")

## look for:
 - idf formula components
 - bm25 fomula components

 ## todo:
 - save indexing records on i/o disc
 ```python
 index_data: BM25Index = {
    # 1. Term counts per chunk
    "term_freqs": [
        {"def": 1, "parse": 1, "config": 1},  # Chunk 0
        {"block": 2, "cache": 1}              # Chunk 1
    ],
    
    # 2. Length of each chunk in tokens
    "doc_lens": [3, 3],
    
    # 3. Overall average length
    "avg_dl": 3.0,
    
    # 4. IDF weight table for every unique term in your codebase
    "idf": {
        "def": 0.18,
        "parse": 0.69,
        "config": 0.69,
        "block": 0.18,
        "cache": 0.69
    },
    
    # 5. Raw chunk strings (so search can map back to source text)
    "chunks": [
        "def parse_config(): ...",
        "block cache block read"
    ]
}
```