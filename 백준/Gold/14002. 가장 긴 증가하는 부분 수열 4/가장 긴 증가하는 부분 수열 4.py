N = int(input())
A = [int(i) for i in input().split()]

dp = [1 for _ in range(N)]
last_max_idx = [-1 for _ in range(N)] # 직전의 가장 긴 부분의 마지막 index를 저장 (역순으로 따라가게끔)

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = max(dp[i], dp[j] + 1)
                last_max_idx[i] = j

res = []
last_idx = dp.index(max(dp))

while last_idx != -1:
    res.append(A[last_idx])
    last_idx = last_max_idx[last_idx]

print(max(dp))
print(*res[::-1])