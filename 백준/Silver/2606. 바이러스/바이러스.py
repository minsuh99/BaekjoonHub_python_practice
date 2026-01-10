import sys

N = int(input())
graph = [[] for _ in range(N + 1)]
edges = int(input())

for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(N + 1)]
res = []
def dfs(node):
    global res
    visited[node] = True
    
    for next_node in graph[node]:
        if not visited[next_node]:
            res.append(next_node)
            dfs(next_node)

dfs(1)
print(len(res))