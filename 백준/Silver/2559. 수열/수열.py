import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num_list = [int(i) for i in input().split()]
partial_sum = [0] * (N + 1)
for i in range(N):
    partial_sum[i] = partial_sum[i - 1] + num_list[i]

res = [0] * (N - K + 1)
res[0] = partial_sum[K - 1]

for i in range(N - K):
    res[i + 1] = partial_sum[i + K] - partial_sum[i]

print(max(res))