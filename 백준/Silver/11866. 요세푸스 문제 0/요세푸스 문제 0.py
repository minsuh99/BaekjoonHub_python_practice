from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
my_queue = deque([int(i) for i in range(1, N + 1)])
res = []

while my_queue:
    my_queue.rotate(-(K - 1))
    res.append(my_queue.popleft())

print(f"<{", ".join([str(i) for i in res])}>")