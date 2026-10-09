import os
from pathlib import Path

for root, sub, files in os.walk("."):
    for file in files:
        print(Path(file).suffix.lower())
