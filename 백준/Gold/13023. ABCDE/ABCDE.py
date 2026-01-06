import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
    
def dfs(node, depth):
    if depth == 4:
        print(1)
        exit()

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, depth + 1)
            visited[next_node] = False

for i in range(N):
    visited = [False for _ in range(N)]
    visited[i] = True
    dfs(i, 0)
    
print(0)
