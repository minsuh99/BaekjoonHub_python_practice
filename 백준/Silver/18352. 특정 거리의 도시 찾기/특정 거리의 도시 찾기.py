import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
dist = [0 for _ in range(N + 1)]
queue = deque()

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)

def bfs(graph, start, visited, dist):
    queue.append(start)
    visited[start] = True
    
    while queue:
        cur_node = queue.popleft()
        for node in graph[cur_node]:
            if visited[node] == False:
                visited[node] = True
                dist[node] = dist[cur_node] + 1
                queue.append(node)

bfs(graph, X, visited, dist)

res = [i for i, num in enumerate(dist) if num == K]
if len(res) == 0:
    print(-1)
else:
    for node in res:
        print(node)