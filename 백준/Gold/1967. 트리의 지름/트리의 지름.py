from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

n = int(input())

adj_list = defaultdict(list)
for _ in range(n-1):
    u, v, value = map(int, input().split())
    adj_list[u].append((v, value))
    adj_list[v].append((u, value))

def dfs(node, visited, distance):
    visited.add(node)
    max_node, max_dist = node, distance
    for neighbor, d in adj_list.get(node, []):
        if neighbor not in visited:
            node_, dist_ = dfs(neighbor, visited, distance + d)
            if dist_ > max_dist:
                max_node, max_dist = node_, dist_
    return max_node, max_dist

visited = set()
max_node, _ = dfs(1, visited, 0)
visited2 = set()
_, max_dist = dfs(max_node, visited2, 0)
print(max_dist)
