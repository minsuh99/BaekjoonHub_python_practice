from collections import deque

N, M = map(int, input().split())
maps = [[0 for _ in range(M)] for _ in range(N)]
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    temp = input()
    maps[i] = [int(j) for j in temp]

def bfs(start_x, start_y, maps):
    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, 1)])
    
    while queue:
        x, y, dist = queue.popleft()
        if x == N - 1 and y == M - 1:
            return dist
        
        for move in dxdy:
            x_ = x + move[0]
            y_ = y + move[1]
            if 0 <= x_ < N and 0 <= y_ < M:
                if (x_, y_) not in visited:
                    if maps[x_][y_] == 1:
                        visited.add((x_, y_))
                        queue.append((x_, y_, dist + 1))
        


print(bfs(0, 0, maps))