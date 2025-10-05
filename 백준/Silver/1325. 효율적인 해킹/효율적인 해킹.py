import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
res = [0 for _ in range(N + 1)]
queue = deque()

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

def bfs(graph, start):
    visited = [False for _ in range(N + 1)]
    global res
    queue.append(start)
    visited[start] = True
    cnt = 1
    
    while queue:
        cur_node = queue.popleft()
        for node in graph[cur_node]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
                cnt += 1
    
    return cnt

for node in range(1, N+1):
    res[node] = bfs(graph, node)
    
max_hack = max(res)
res = [i for i in range(1, N + 1) if res[i] == max_hack]
print(*res)