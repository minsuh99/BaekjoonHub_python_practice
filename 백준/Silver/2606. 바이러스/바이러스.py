N = int(input())
T = int(input())

computers = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(T):
    a, b = map(int, input().split())
    computers[a][b] = 1
    computers[b][a] = 1

def dfs(graph, node, visited):
    visited[node] = True
    for i in range(len(graph[node])):
        if graph[node][i] == 1:
            if visited[i] == False:
                visited[i] = True
                dfs(graph, i, visited)

dfs(computers, 1, visited)
print(sum(visited) - 1)