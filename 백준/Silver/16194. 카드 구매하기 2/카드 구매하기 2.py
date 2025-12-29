N = int(input())
P = [0] + [int(i) for i in input().split()]

dp = [10000000 for _ in range(N + 1)]
for i in range(len(P)):
    dp[i] = P[i]

for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i - j] + P[j], dp[i])

print(dp[N])