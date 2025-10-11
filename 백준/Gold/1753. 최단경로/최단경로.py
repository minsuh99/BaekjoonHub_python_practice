import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
dist = [float('inf') for _ in range(V + 1)]
queue = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

queue.put((0, K))
dist[K] = 0

while queue.qsize() > 0:
    cur = queue.get()
    cur_v = cur[1]
    if visited[cur_v]:
        continue
    visited[cur_v] = True
    
    for temp in graph[cur_v]:
        next_node, weight = temp[0], temp[1]
        if dist[next_node] > dist[cur_v] + weight:
            dist[next_node] = dist[cur_v] + weight
            queue.put((dist[next_node], next_node))

for d in dist[1:]:
    print(d if d != float('inf') else "INF")