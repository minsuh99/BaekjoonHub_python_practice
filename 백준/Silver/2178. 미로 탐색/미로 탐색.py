from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(N):
    board[i] = list(map(int, input().rstrip()))
    

def bfs(r, c):
    visited[r][c] = True
    queue = deque([(r, c, 1)])

    while queue:
        cur_r, cur_c, length = queue.popleft()
        if cur_r == N - 1 and cur_c == M - 1:
            return length
        for dr, dc in drdc:
            nr = cur_r + dr
            nc = cur_c + dc
            
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and board[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc, length + 1))

print(bfs(0, 0))