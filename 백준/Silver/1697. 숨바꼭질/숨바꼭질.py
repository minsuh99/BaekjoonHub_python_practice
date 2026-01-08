from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False for _ in range(100001)]


def bfs(cur, cnt):
    visited[cur] = True
    queue = deque([(cur, cnt)])
    
    while queue:
        pos, c = queue.popleft()
        if pos == K:
            print(c)
            return

        for new_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= new_pos <= 100000 and not visited[new_pos]:
                visited[new_pos] = True
                queue.append((new_pos, c + 1))
bfs(N, 0)