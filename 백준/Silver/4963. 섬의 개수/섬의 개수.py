import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()
        
    board = [[] for _ in range(h)]
    
    drdc = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    res = []
    
    for i in range(h):
        board[i] = list(map(int, input().split()))

    
    def dfs(cur_r, cur_c):
        visited[cur_r][cur_c] = True
        area = 1
        
        for dr, dc in drdc:
            nr = cur_r + dr
            nc = cur_c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if visited[nr][nc] == False and board[nr][nc] == 1:
                    area += dfs(nr, nc)
        
        return area
    
    for r in range(h):
        for c in range(w):
            if visited[r][c] == False and board[r][c] == 1:
                res.append(dfs(r, c))
    
    print(len(res))