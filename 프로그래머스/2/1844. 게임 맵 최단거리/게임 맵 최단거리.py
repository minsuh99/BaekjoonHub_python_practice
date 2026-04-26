from collections import deque


def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    
    def bfs():
        nonlocal n, m
        nonlocal visited
        nonlocal drdc
        visited[0][0] = True
        queue = deque([(0, 0, 1)])
        
        while queue:
            r, c, cnt = queue.popleft()
            if r == n - 1 and c == m - 1:
                return cnt
            for dr, dc in drdc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if not visited[nr][nc] and maps[nr][nc] == 1:
                        visited[nr][nc] = True
                        queue.append((nr, nc, cnt + 1))
        
        return -1
    
    return bfs()