from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
virus = []
drdc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))

def backtracking(start, count):
    global res
    if count == 3:
        cnt = bfs()
        res = max(res, cnt)
        return
    
    for i in range(start, N * M):
        r = i // M
        c = i % M
        if board[r][c] == 0:
            board[r][c] = 1
            backtracking(i + 1, count + 1)
            board[r][c] = 0


def bfs():
    temp = [row[:] for row in board]
    queue = deque(virus)
    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for r, c in virus:
        visited[r][c] = True
    
    while queue:
        vr, vc = queue.popleft()
        
        for dr, dc in drdc:
            nr = vr + dr
            nc = vc + dc
            
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc]:
                    if temp[nr][nc] == 0:
                        visited[nr][nc] = True
                        temp[nr][nc] = 2
                        queue.append((nr, nc))
    
    for r in range(N):
        for c in range(M):
            if temp[r][c] == 0:
                cnt += 1
    
    return cnt

backtracking(0, 0)
print(res)