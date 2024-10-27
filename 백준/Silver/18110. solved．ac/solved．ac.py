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

# 파이썬의 round()가 오사오입 방식인지 처음 알았다..
# math.floor(x + 0.5)를 이용하면 제대로 반올림이 된다.. 
# 대신 정수 범위일때만
