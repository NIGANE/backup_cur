source = "line 1\n line2\n\nline3\nline4"
lines = [line for line in source.splitlines(True) if len(line) > 1]
print(lines)