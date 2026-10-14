from chunker import Chunker


def main():
    max_size = 2000
    chunker = Chunker()
    files = chunker.discover_files("test")
    chunks = []
    print("-- discoverd files: ", "---" * 10)
    for f in files:
        print("file location: ", f[0], f"{len(f[1])} bytes")
        chunks = [*chunker.chunk_document(f[0], f[1]), *chunks]
    print("-- chunks files: ", "---" * 10)
    for ch in chunks:
        print(f"path: {ch[0].file_path} ",
              f"({ch[0].first_character_index}",
              f"-{ch[0].last_character_index}) ",
              f"{len(ch[1])} bytes",
              sep="")
    chunker.save()


main()
