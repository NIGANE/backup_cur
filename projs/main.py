import re
import sys

pattern = re.compile(
    r"^nb_drones:\s(?P<count>\d+)$")

data = []
with open(sys.argv[1], "r") as f:
    data = f.readlines()

for i, line in enumerate(data):
    if (line.startswith("nb_drones")):
        # print(line)
        match = re.search(pattern, line)
        print(match)
        if match:
            print(line)
            print(match.groupdict())
