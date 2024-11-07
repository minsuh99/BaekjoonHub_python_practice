import sys

n, k = map(int, sys.stdin.readline().split())
coin_list = []

for _ in range(n):
    coin_list.append(int(sys.stdin.readline()))

res = 0
for money in coin_list[::-1]:
    if k // money == 0:
        continue
    res += (k // money)
    k %= money

print(res)