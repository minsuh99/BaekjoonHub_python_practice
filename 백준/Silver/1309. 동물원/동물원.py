N = int(input())

dp = [[0 for _ in range(3)] for _ in range(N + 1)]
dp[0][0] = 1

# dp[i][0] = 이전 행에 아무것도 안 놓은거
# dp[i][1] = 이전 행에서 왼쪽 열에 놓은거
# dp[i][2] = 이전 행에서 오른쪽 열에 놓은거

for i in range(1, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[N]) % 9901)