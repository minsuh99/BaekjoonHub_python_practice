import sys
input = sys.stdin.readline

dp = [1] + [0 for _ in range(1, 1000001)]
for i in range(1, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

T = int(input())
for _ in range(T):
    print(dp[int(input())] % 1000000009)
