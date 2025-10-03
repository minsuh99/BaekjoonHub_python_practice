from collections import deque
import sys
input = sys.stdin.readline

V = int(input())

graph = [[] for _ in range(V + 1)]
queue = deque()
visited = [False for _ in range(V + 1)]
dist = [0 for _ in range(V + 1)]

for _ in range(V):
    input_queue = deque(map(int, input().split()))
    node1 = input_queue.popleft()
    while True:
        node2 = input_queue.popleft()
        if node2 == -1:
            break
        weight = input_queue.popleft()
        graph[node1].append((node2, weight))

def bfs(graph, start, dist):
    visited[start] = True
    queue.append(start)

    while queue:
        next_node = queue.popleft()
        for i in graph[next_node]:
            if visited[i[0]] == False:
                visited[i[0]] = True
                queue.append(i[0])
                dist[i[0]] = dist[next_node] + i[1]

bfs(graph, 1, dist)
MAX = 0
next_search_node = 0

for i in range(1, V+1):
    if dist[i] > MAX:
        next_search_node = i
        MAX = dist[i]

dist = [0 for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
bfs(graph, next_search_node, dist)
print(max(dist))