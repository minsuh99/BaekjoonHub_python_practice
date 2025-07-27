import sys

N, M = map(int, sys.stdin.readline().split())
num_list = [[0] * (N + 1)]
for _ in range(N):
    num_list.append([0] + [int(i) for i in sys.stdin.readline().split()])
partial_sum_list = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N +1):
        partial_sum_list[i][j] += partial_sum_list[i-1][j] + partial_sum_list[i][j-1] - partial_sum_list[i-1][j-1] + num_list[i][j]
                
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(partial_sum_list[x2][y2] - partial_sum_list[x2][y1 - 1] - partial_sum_list[x1 - 1][y2] + partial_sum_list[x1 - 1][y1 - 1])