dp = [[0 for _ in range(2)] for _ in range(91)]
dp[1][1] = 1

for i in range(2, 91):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]
    
N = int(input())
print(sum(dp[N]))