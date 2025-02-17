def min_dist_node(N, visited, dist):
    min_dist = float("inf")
    node = 0
    
    for i in range(1, N+1):
        if dist[i] < min_dist and not visited[i]:
            min_dist = dist[i]
            node = i
    return node



def solution(N, road, K):
    answer = 0
    graph = [[float("inf") for _ in range(N + 1)] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    dist = [float("inf") for _ in range(N + 1)]
    graph[1][1] = 0
    visited[1] = True
    
    for r in road:
        node1, node2, w = map(int, r)
        if graph[node1][node2] > w:
            graph[node1][node2] = w
            graph[node2][node1] = w
            
    start_node = 1
    
    for i in range(1, N + 1):
        if graph[start_node][i] != float("inf"):
            dist[i] = graph[start_node][i]
            
    for i in range(1, N + 1):
        min_node = min_dist_node(N, visited, dist)
        visited[min_node] = True
            
        for j in range(1, N + 1):
            if graph[min_node][j] != float("inf") \
            and dist[min_node] + graph[min_node][j] < dist[j]:
                dist[j] = dist[min_node] + graph[min_node][j]
        
    
    answer = sum([True for d in dist if d <= K])
    return answer