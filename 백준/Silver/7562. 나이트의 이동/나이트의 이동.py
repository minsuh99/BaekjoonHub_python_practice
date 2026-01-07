from collections import deque
import sys
input = sys.stdin.readline

drdc = [(1, 2), (-1, 2), (2, 1), (-2, 1), (1, -2), (-1, -2), (2, -1), (-2, -1)]

T = int(input())

for _ in range(T):
    I = int(input())
    
    start_r, start_c = map(int, input().split())
    des_r, des_c = map(int, input().split())
    visited = [[False for _ in range(I)] for _ in range(I)]
    
    queue = deque([(start_r, start_c, 0)])
    visited[start_r][start_c] = True
    
    while queue:
        r, c, length = queue.popleft()
        if r == des_r and c == des_c:
            print(length)
            break
            
        for dr, dc in drdc:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < I and 0 <= nc < I:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, length + 1))
    
