N = int(input())
A = [int(i) for i in input().split()]
dp_nondel = [0 for _ in range(N)]
dp_del = [0 for _ in range(N)]

dp_nondel[0] = A[0]
dp_del[0] = -1001

for i in range(1, N):
    dp_nondel[i] = max(A[i], dp_nondel[i-1] + A[i])

for i in range(1, N):
    dp_del[i] = max(dp_nondel[i - 1], dp_del[i - 1] + A[i])

print(max(max(dp_nondel), max(dp_del)))