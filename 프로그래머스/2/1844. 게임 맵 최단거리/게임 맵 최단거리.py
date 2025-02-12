from collections import deque
# 혼자 짜보기 (bfs 이용 최단거리 찾기)
# def bfs(start_x, start_y, end_x, end_y, maps): 
# 기존에 이렇게 짰는데, [목표지점] end_x, end_y가 maps의 오른쪽 하단점으로 고정이라 없어도 될 듯
def bfs(start_x, start_y, maps):
    n = len(maps)
    m = len(maps[0])
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, 1)])
    
    while queue:
        x, y, dist = queue.popleft()
        if x == n -1 and y == m - 1:
            return dist
        for d in dxdy:
            x_, y_ = x + d[0], y + d[1]
            if 0 <= x_ < n and 0 <= y_ < m:
                if (x_, y_) not in visited:
                    if maps[x_][y_] == 1:
                        visited.add((x_, y_))
                        queue.append((x_, y_, dist + 1))
    return -1
    
    

def solution(maps):
    answer = bfs(0, 0, maps)
    return answer