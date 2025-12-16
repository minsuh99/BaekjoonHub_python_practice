T = int(input())
coins = [25, 10, 5, 1]

for _ in range(T):
    C = int(input())
    res = []
    for coin in coins:
        res.append(C//coin)
        C %= coin
    print(*res)