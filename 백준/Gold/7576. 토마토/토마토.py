from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = [[] for _ in range(N)]
drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
res = 0
queue = deque()

for i in range(N):
    board[i] = list(map(int, input().split()))
    
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            queue.append((r, c, 0))

while queue:
    cur_r, cur_c, day = queue.popleft()
    res = max(res, day)

    for dr, dc in drdc:
        nr = cur_r + dr
        nc = cur_c + dc
        
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 0:
                board[nr][nc] = 1
                queue.append((nr, nc, day + 1))

for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            print(-1)
            exit()

print(res)