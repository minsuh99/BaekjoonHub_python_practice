from collections import deque

N, M, V = map(int, input().split())
visited_dfs = [0 for _ in range(N + 1)] # visited = set() 해도 될듯
visited_bfs = [0 for _ in range(N + 1)]

inf = float('inf')
graph = [[inf for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

res_dfs = []
res_bfs = []
    
def dfs(graph, node, visited):
    visited[node] = 1
    res_dfs.append(node)
        
    for n in range(1, N + 1):
        if graph[node][n] == 1:
            if visited[n] != 1:
                dfs(graph, n, visited)
        
    return res_dfs

def bfs(graph, node, visited):
    visited[node] = 1
    queue = deque([node])
    res_bfs.append(node)
    
    while queue:
        node_ = queue.popleft()
        for i in range(len(graph[node_])):
            if graph[node_][i] == 1:
                if visited[i] != 1:
                    visited[i] = 1
                    res_bfs.append(i)
                    queue.append(i)
    
    return res_bfs
    

print(*dfs(graph, V, visited_dfs))
print(*bfs(graph, V, visited_bfs))