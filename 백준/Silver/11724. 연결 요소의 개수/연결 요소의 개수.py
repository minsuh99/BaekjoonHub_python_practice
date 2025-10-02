import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
res = 0

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def dfs(graph, start, visited):
    visited[start] = True
    
    for node in graph[start]:
        if visited[node] == False:
            dfs(graph, node, visited)

for node in range(1, N+1):
    if not visited[node]:
        res += 1
        dfs(graph, node, visited)

print(res)
