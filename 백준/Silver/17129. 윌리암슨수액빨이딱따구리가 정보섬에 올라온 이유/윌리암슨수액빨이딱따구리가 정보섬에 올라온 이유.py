from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

maps = [[0 for _ in range(M)] for _ in range(N)]
start_x, start_y = 0, 0
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


for i in range(N):
    temp = input().rstrip()
    if "2" in temp:
        start_x, start_y = i, temp.index("2")
    maps[i] = [int(j) for j in temp]

def bfs(start_x, start_y, maps):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[start_x][start_y] = 1
    queue = deque([(start_x, start_y, 0)])

    
    while queue:
        x, y, dist = queue.popleft()
        if maps[x][y] in [3, 4, 5]:
            return dist
        
        for move in dxdy:
            x_, y_ = x + move[0], y + move[1]
            if 0 <= x_ < N and 0 <= y_ < M:
                if maps[x_][y_] in [0, 3, 4, 5]:
                    if visited[x_][y_] != 1:
                        visited[x_][y_] = 1
                        queue.append((x_, y_, dist + 1))
                        
    return -1

res = bfs(start_x, start_y, maps)
if res == -1:
    print("NIE")
else:
    print("TAK")
    print(res)