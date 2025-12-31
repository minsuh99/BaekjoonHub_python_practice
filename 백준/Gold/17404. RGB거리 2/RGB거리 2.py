import sys
input = sys.stdin.readline

N = int(input())
rgb = [[] for _ in range(N)]
res = 1000001


for i in range(N):
    rgb[i] = list(map(int, input().split()))

for i in range(3):
    dp = [[1001 for _ in range(3)] for _ in range(N)]
    dp[0][i] = rgb[0][i]
    
    for j in range(1, N):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + rgb[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + rgb[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + rgb[j][2]
    
    for k in range(3):
        if i != k:
            res = min(res, dp[-1][k])

print(res)