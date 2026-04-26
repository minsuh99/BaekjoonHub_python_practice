from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def bfs(node):
        nonlocal visited, n, computers
        queue = deque([node])
        
        while queue:
            next_node = queue.popleft()
            visited[next_node] = True
            for i in range(n):
                if not visited[i]:
                    if computers[next_node][i] == 1 and next_node != i:
                        queue.append(i)

    for node in range(n):
        if visited[node] == False:
            bfs(node)
            answer += 1
    
    return answer