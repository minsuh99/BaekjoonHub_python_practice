from collections import defaultdict, deque

def bfs(start_x, start_y, maps):
    n = len(maps)
    res = []
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set([(start_x, start_y, "")])
    queue = deque([(start_x, start_y, "", 0)])
    cost = defaultdict(lambda :float("inf"))
    cost[(0, 0, '')] = 0
    

    while queue:
        queue = deque(sorted(queue, key=lambda x:x[3]))
        x, y, direction, dist = queue.popleft()
        if cost[(x, y, direction)] and dist > cost[(x, y, direction)]:
            continue
        
        if x == n - 1 and y == n - 1:
            res.append(dist)
            
        for d in dxdy:
            if d in [(-1, 0), (1, 0)]:
                new_dir = "ver"
            else:
                new_dir = "hor"
            x_, y_ = x + d[0], y + d[1]
            if 0 <= x_ < n and 0 <= y_ < n and maps[x_][y_] == 0:
                if direction == "" or direction == new_dir:
                    dist_ =  dist + 1
                else:
                    dist_ = dist + 6
            
                if dist_ < cost[(x_, y_, new_dir)]:
                    cost[(x_, y_, new_dir)] = dist_
                    queue.append((x_, y_, new_dir, dist_))
    return res

def solution(board):
    answer = min(bfs(0, 0, board)) * 100
    return answer