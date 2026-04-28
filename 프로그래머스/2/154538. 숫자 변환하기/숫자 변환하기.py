from collections import deque


def solution(x, y, n):
    visited = [False for _ in range(y + 1)]
    queue = deque([(x, 0)])
    
    while queue:
        cur_x, cnt = queue.popleft()
        if cur_x == y:
            return cnt
        
        elif cur_x < y and not visited[cur_x]:
            visited[cur_x] = True
            queue.append((cur_x + n, cnt + 1))
            queue.append((cur_x * 2, cnt + 1))
            queue.append((cur_x * 3, cnt + 1))
    
    return -1