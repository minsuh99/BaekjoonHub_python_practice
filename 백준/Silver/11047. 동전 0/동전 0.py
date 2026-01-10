import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
res = 0

for _ in range(N):
    coin.append(int(input()))

for i in range(N - 1, -1, -1):
    res += K // coin[i]
    K %= coin[i]
    
    if K == 0:
        break

print(res)