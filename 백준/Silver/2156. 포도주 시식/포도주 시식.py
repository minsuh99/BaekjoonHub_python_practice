import sys

n = int(input())
grape = []
for _ in range(n):
    grape.append(int(input()))

dp = [[-1 for _ in range(3)] for _ in range(n)]
dp[0][0] = 0
dp[0][1] = grape[0]
dp[0][2] = grape[0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = dp[i - 1][0] + grape[i]
    dp[i][2] = dp[i - 1][1] + grape[i]

print(max(dp[n - 1]))