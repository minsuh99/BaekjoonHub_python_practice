from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().rstrip())))

visited = [[False for _ in range(M)] for _ in range(N)]
drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# (cur_r, cur_c, wall)
queue = deque([(0, 0, 0)])
visited[0][0] = True

while queue:
    cur_r, cur_c, wall = queue.popleft()
    if cur_r == N - 1 and cur_c == M - 1:
        print(wall)
        exit()
    
    for dr, dc in drdc:
        nr = cur_r + dr
        nc = cur_c + dc
        
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                if board[nr][nc] == 0:
                    queue.appendleft((nr, nc, wall))
                elif board[nr][nc] == 1:
                    queue.append((nr, nc, wall + 1))
    