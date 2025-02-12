from collections import deque



def bfs(start_x, start_y, end_x, end_y, maps):
    row = len(maps)
    col = len(maps[0])
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, 0)])
    
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == end_x and y == end_y:
            return dist
        
        for d in dxdy:
            x_, y_ = x + d[0], y + d[1]
            
            if 0 <= x_ < row and 0 <= y_ < col:
                if (x_, y_) not in visited:
                    if maps[x_][y_] in ["S", "L", "O", "E"]:
                        visited.add((x_, y_))
                        queue.append((x_, y_, dist+1))
    
    return -1

def solution(maps):
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == "S":
                sx, sy = x, y
            elif maps[x][y] == "L":
                lx, ly = x, y
            elif maps[x][y] == "E":
                ex, ey = x, y
    
    dist1 = bfs(sx, sy, lx, ly, maps)
    dist2 = bfs(lx, ly, ex, ey, maps)
    
    if dist1 != -1 and dist2 != -1:
        return dist1 + dist2
    else:
        return -1