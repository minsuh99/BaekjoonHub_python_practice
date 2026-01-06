from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
res_dfs = []
res_bfs = []

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, N + 1):
    graph[i].sort()


def dfs(node, visited):
    visited[node] = True
    res_dfs.append(node)
    
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        res_bfs.append(node)
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

visited_dfs = [False for _ in range(N + 1)]
visited_bfs = visited_dfs.copy()

dfs(V, visited_dfs)
bfs(graph, V, visited_bfs)
print(*res_dfs)
print(*res_bfs)