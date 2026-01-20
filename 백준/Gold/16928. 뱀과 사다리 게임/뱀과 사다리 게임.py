from collections import deque, defaultdict
import sys
input = sys.stdin.readline

my_dict = defaultdict(int)

N, M = map(int, input().split())
for _ in range(N + M):
    s, e = map(int, input().split())
    my_dict[s] = e

queue = deque([(1, 0)]) # (pos, cnt)
visited = [False for _ in range(101)]
visited[1] = True

while queue:
    pos, cnt = queue.popleft()
    if pos == 100:
        print(cnt)
        exit()
    
    for i in range(6, 0, -1):
        if 1 <= pos + i <= 100:
            new_pos = pos + i
        while True:
            if new_pos not in my_dict.keys():
                break
            new_pos = my_dict[new_pos]
        if not visited[new_pos]:
            visited[new_pos] = True
            queue.append((new_pos, cnt + 1))