from collections import deque
import sys
input = sys.stdin.readline

def round(num):
    if 0 <= num - int(num) < 0.5:
        return int(num)
    elif num - int(num) >= 0.5:
        return int(num) + 1

n = int(input())
if n == 0:
    print(0)
    exit()
level = deque()

for _ in range(n):
    level.append(int(input()))
level = deque(sorted(level))

del_num = round(n * 0.15)

for _ in range(del_num):
    level.popleft()
    level.pop()

print(round(sum(level) / len(level)))