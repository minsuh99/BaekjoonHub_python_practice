# from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
board = [[] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
res = []

for i in range(N):
    board[i] = list(map(int, input().rstrip()))


# def bfs(cur_r, cur_c):
#     visited[cur_r][cur_c] = True
#     queue = deque([(cur_r, cur_c)])
#     area = 1
    
#     while queue:
#         r, c = queue.popleft()
#         for dr, dc in drdc:
#             if 0 <= r + dr < N and 0 <= c + dc < N:
#                 if visited[r + dr][c + dc] == False and board[r + dr][c + dc] == 1:
#                     visited[r + dr][c + dc] = True
#                     queue.append((r + dr, c + dc))
#                     area += 1
#     return area

def dfs(cur_r, cur_c):
    visited[cur_r][cur_c] = True
    area = 1
    for dr, dc in drdc:
        if 0 <= cur_r + dr < N and 0 <= cur_c + dc < N:
            if not visited[cur_r + dr][cur_c + dc] and board[cur_r + dr][cur_c + dc] == 1:
                area += dfs(cur_r + dr, cur_c + dc)
    return area


for r in range(N):
    for c in range(N):
        if visited[r][c] == False and board[r][c] == 1:
            # res.append(bfs(r, c))
            res.append(dfs(r, c))

res.sort()
print(len(res))
for ans in res:
    print(ans)