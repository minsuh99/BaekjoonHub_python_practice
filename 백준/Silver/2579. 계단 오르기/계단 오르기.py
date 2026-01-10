import sys
input = sys.stdin.readline

N = int(input())
stairs = []
dp = [[0 for _ in range(3)] for _ in range(N)]
# dp[_][1] = 해당 계단까지 1번 연속으로 밟았을 때,
# dp[_][2] = 해당 계단까지 2번 연속으로 밟았을 때,

for _ in range(N):
    stairs.append(int(input()))

if N == 1:
    print(stairs[0])
    exit()

dp[0][1] = stairs[0]
dp[1][1] = stairs[1]
dp[1][2] = stairs[0] + stairs[1]


for i in range(2, N):
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + stairs[i]
    dp[i][2] = dp[i - 1][1] + stairs[i]

print(max(dp[-1]))