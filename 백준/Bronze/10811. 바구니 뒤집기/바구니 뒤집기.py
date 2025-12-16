N, M = map(int, input().split())
res = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    idx1, idx2 = i - 1, j - 1
    while True:
        if idx1 >= idx2:
            break
        res[idx1], res[idx2] = res[idx2], res[idx1]
        idx1 += 1
        idx2 -= 1

print(*res)