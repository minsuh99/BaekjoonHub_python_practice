import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
partial_sum = [0 for _ in range(N + 1)]

for k in range(1, N + 1):
    partial_sum[k] = partial_sum[k - 1] + num_list[k]

for _ in range(M):
    i, j = map(int, input().split())
    print(partial_sum[j] - partial_sum[i - 1])