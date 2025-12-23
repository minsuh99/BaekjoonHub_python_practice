from collections import deque

N, K = map(int, input().split())

queue = deque([int(i) for i in range(1, N + 1)])
res = []
while queue:
    queue.rotate(-K + 1)
    res.append(str(queue.popleft()))

print("<" + ", ".join(res) + ">")