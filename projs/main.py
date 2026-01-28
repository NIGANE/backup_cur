import time
import sys
print("err 1", file=sys.stderr, end="", flush=True)
time.sleep(2)
print("err 2", file=sys.stderr)