from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        u, v = e[0], e[1]
        graph[u].append(v)
        graph[v].append(u)
    visited = [False for _ in range(n + 1)]
    INF = float("inf")
    dist = [INF for _ in range(n + 1)]
    dist[1] = 0
    
    queue = deque([(1, 0)]) # (node, dist)
    
    while queue:
        node, d = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        dist[node] = d
        
        for next_node in graph[node]:
            queue.append((next_node, d + 1))
    
    max_dist = max(dist[1:])
    print(dist, max_dist)
    for i in range(1, n + 1):
        if dist[i] == max_dist:
            answer += 1
    
    return answer