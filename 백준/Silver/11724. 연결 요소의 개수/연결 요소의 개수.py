import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(node, visited):
    visited[node] = True
    
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited)
    

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, visited)
        cnt += 1

print(cnt)