N = int(input())
P = [0] + [int(i) for i in input().split()]

dp = [0 for _ in range(N + 1)]
dp[1] = P[1]

for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i - j] + P[j], dp[i])

print(dp[N])