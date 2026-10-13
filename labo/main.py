import ast
from pydantic import BaseModel


class MinimalSource(BaseModel):
    file_path: str
    first_character_index: int
    last_character_index: int


def blind_chunking(source: str, max_size: int) -> list:
    print("calling for blind_chunking func")
    return []


def inspect_chunks(chunks: list, source:str = None) -> None:
    for i, ch in enumerate(chunks):
        ob = ch[0]
        txt = ch[1]
        print(f"chunk {i + 1}: {len(txt)} chars")
        print(f"chars: {ob.first_character_index} - {ob.last_character_index}")
        # print(f"repr: ({txt[0]}) - ({txt[len(txt) - 1]})")


def python_chunking(file: str, content: str, max_size: int
                    ) -> list:
    start_char: int = 0
    chunks: list = []
    last_end: int = 0

    try:
        tree = ast.parse(content)
    except Exception:
        blind_chunking(content, max_size)

    nodes = [node for node in tree.body
             if isinstance(node, (ast.FunctionDef,
                                  ast.ClassDef, ast.AsyncFunctionDef))]
    if (not nodes):
        return blind_chunking(content, max_size)
    lines = content.splitlines(True)

    for node in nodes:
        chunk = ''
        i = node.lineno - 1
        context = []
        start = sum(len(lines[i]) for i in range(node.lineno - 1))
        end = sum(len(lines[i]) for i in range(node.end_lineno))
        print(f"lines: {node.lineno} - {node.end_lineno}")
        print("strt: ", start)
        print("end: ", end)

        while i < node.end_lineno:
            context.append(lines[i])
            i += 1
        chunk = ''.join(context)
        if (len(chunk) > max_size):
            chunks.extend(blind_chunking(chunk, max_size))
        else:
            source = MinimalSource(
                    file_path=target_file,
                    first_character_index=start_char,
                    last_character_index=start_char + len(chunk) - 1
                )
            chunks.append((source, chunk))
        start_char += len(chunk)
    return (chunks)


target_file = "./target.py"
max_size = 2000
content = ""
chunks = []

try:
    with open(target_file, "r") as f:
        content = f.read()
    chunks = [*python_chunking(target_file, content, max_size), *chunks]
    # inspect_chunks(chunks)
except Exception as e:
    print(f"Error: {e}")
