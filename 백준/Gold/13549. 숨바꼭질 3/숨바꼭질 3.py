from collections import deque

N, K = map(int, input().split())
visited = [False for _ in range(100001)]
queue = deque([(N, 0)])
visited[N] = True

while queue:
    pos, t = queue.popleft()
    if pos == K:
        print(t)
        exit()
        
    if pos * 2 <= 100000 and not visited[pos * 2]:
        visited[pos * 2] = True
        queue.append((pos * 2, t))
    
    if pos - 1 >= 0 and not visited[pos - 1]:
        visited[pos - 1] = True
        queue.append((pos - 1, t + 1))
    
    if pos + 1 <= 100000 and not visited[pos + 1]:
        visited[pos + 1] = True
        queue.append((pos + 1, t + 1))