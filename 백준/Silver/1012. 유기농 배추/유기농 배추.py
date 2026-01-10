from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    res = 0
    for _ in range(K):
        c, r = map(int, input().split())
        board[r][c] = 1
    
    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        
        while queue:
            cur_r, cur_c = queue.popleft()
            visited[cur_r][cur_c] = True
            
            for dr, dc in drdc:
                nr = cur_r + dr
                nc = cur_c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if not visited[nr][nc]:
                        if board[nr][nc] == 1:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] == 1:
                bfs(i, j)
                res += 1
    print(res)