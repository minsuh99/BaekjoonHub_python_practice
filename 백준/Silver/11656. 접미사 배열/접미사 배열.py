from collections import deque
import sys
input = sys.stdin.readline

S = input().rstrip()
res = []
my_queue = deque(S)

while my_queue:
    res.append("".join(my_queue))
    my_queue.popleft()

for end in sorted(res):
    print(end)