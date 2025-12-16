N, M = map(int, input().split())
res = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    res[i - 1], res[j - 1] = res[j - 1], res[i - 1]

print(*res)