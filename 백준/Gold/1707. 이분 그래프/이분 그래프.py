from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    colors = [0 for _ in range(V + 1)]
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    
    def bfs(start, colors):
        queue = deque([start])
        colors[start] = 1
        
        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                if colors[next_node] == 0:
                    colors[next_node] = 3 - colors[node]
                    queue.append(next_node)
                else:
                    if colors[next_node] == colors[node]:
                        return False
        return True
    
    flag = True
    for i in range(1, V + 1):
        if colors[i] == 0:
            if not bfs(i, colors):
                flag = False
                break
    
    print("YES" if flag else "NO")