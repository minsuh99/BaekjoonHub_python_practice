import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
partial_sum = [0] * N
partial_sum[0] = num_list[0]
res_count = [0] * M

for i in range(1, N):
    partial_sum[i] = partial_sum[i - 1] + num_list[i]

cnt = 0

for i in range(N):
    temp = partial_sum[i] % M
    res_count[temp] += 1

cnt += res_count[0]

for i in range(M):
    cnt += res_count[i] * (res_count[i] - 1) // 2

print(cnt)
