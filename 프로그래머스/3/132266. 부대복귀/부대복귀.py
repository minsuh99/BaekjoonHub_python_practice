from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    
    for road in roads:
        u, v = map(int, road)
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start, g):
        dist = [-1 for _ in range(len(g))]
        queue = deque([(start, 0)])
        dist[start] = 0
        visited = [False for _ in range(len(g))]
        
        while queue:
            node, cnt = queue.popleft()
            if dist[node] == -1:
                dist[node] = cnt
            visited[node] = True
            
            for next_node in g[node]:
                if not visited[next_node]:
                    queue.append((next_node, cnt + 1))
                    
        return dist
    
    result = bfs(destination, graph)
    for source in sources:
        answer.append(result[source])
        
    return answer
