import sys
import math

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    level = []

    for _ in range(n):
        level.append(int(sys.stdin.readline()))

    level.sort()
    cut = int(math.floor(n * 0.15 + 0.5))
    level = level[cut:(len(level)-cut)]

    print(math.floor(sum(level) / len(level) + 0.5))