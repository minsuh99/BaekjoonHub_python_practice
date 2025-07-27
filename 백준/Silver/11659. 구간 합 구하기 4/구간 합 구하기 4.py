import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_list = [int(i) for i in input().split()]
partial_sum = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    partial_sum[i] = partial_sum[i - 1] + num_list[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(partial_sum[j] - partial_sum[i - 1])