from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
visited = [[False for _ in range(N)] for _ in range(N)]

sr, sc, er, ec = map(int, input().split())

queue = deque([(sr, sc, 0)])
visited[sr][sc] = True
drdc = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]


while queue:
    r, c, cnt = queue.popleft()
    if r == er and c == ec:
        print(cnt)
        exit()
    
    for dr, dc in drdc:
        nr = r + dr
        nc = c + dc
        
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, cnt + 1))

print(-1)