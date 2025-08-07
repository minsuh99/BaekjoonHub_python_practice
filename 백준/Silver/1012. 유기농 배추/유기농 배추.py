import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(graph, cur_y, cur_x, visited):
    visited[cur_y][cur_x] = True
    
    for move in dxdy:
        y_, x_ = cur_y + move[0], cur_x + move[1]
        if 0 <= y_ < N and 0 <= x_ < M:
            if (y_, x_) in graph:
                if visited[y_][x_] == False:
                    visited[y_][x_] = True
                    dfs(graph, y_, x_, visited)

T = int(input())
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    ans = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        cabbages.append((y, x))
        
    for start_y, start_x in cabbages:
        if visited[start_y][start_x] == False:
            dfs(cabbages, start_y, start_x, visited)
            ans += 1
    print(ans)
