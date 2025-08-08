from queue import PriorityQueue
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
distance = [float('inf')] * (V + 1)
visited = [False] * (V + 1)
my_list = [[] for _ in range(V + 1)]
queue = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    my_list[u].append((v, w))

queue.put((0, K))
distance[K] = 0

while queue.qsize() > 0:
    cur = queue.get()
    cur_v = cur[1]
    if visited[cur_v]:
        continue
    visited[cur_v] = True
    
    for temp in my_list[cur_v]:
        next_v, next_w = temp[0], temp[1]
        if distance[next_v] > distance[cur_v] + next_w:
            distance[next_v] = distance[cur_v] + next_w
            queue.put((distance[next_v], next_v))
            

for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")