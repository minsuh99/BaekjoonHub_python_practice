from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False for _ in range(100001)]
parent = [-1 for _ in range(100001)]

def bfs(cur):
    visited[cur] = True
    queue = deque([(cur)])

    while queue:
        pos = queue.popleft()
        if pos == K:
            return

        for new_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= new_pos <= 100000 and not visited[new_pos]:
                visited[new_pos] = True
                parent[new_pos] = pos
                queue.append((new_pos))

bfs(N)
path = []
cur_pos = K

while True:
    if cur_pos == -1:
        break
    path.append(cur_pos)
    cur_pos = parent[cur_pos]

print(len(path) - 1)
print(*path[::-1])