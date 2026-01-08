from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
cycle_node = [False for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
visited_dfs = [False for _ in range(N + 1)]

for _ in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(node, parent):
    visited_dfs[node] = True

    for next_node in graph[node]:
        if next_node == parent:
            continue

        # 아직 방문 안 한 경우
        if not visited_dfs[next_node]:
            res = dfs(next_node, node)

            # 사이클 전파 중
            if res != -1:
                cycle_node[node] = True
                if node == res:
                    return -1  # 사이클 마킹 종료
                else:
                    return res

        # 방문했는데 parent가 아니면 사이클 발견
        else:
            cycle_node[node] = True
            return next_node  # 사이클 시작점 반환

    return -1

dfs(1, -1)


def bfs():
    dist = [-1] * (N + 1)
    queue = deque()

    for i in range(1, N + 1):
        if cycle_node[i]:
            dist[i] = 0
            queue.append(i)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist

dist = bfs()
print(*dist[1:])
    