n = int(input())
d = [0 for _ in range(n + 1)]
d[1] = 0

for i in range(2, n + 1):
    flag1 = (i % 2 != 0)
    flag2 = (i % 3 != 0)
    d[i] = min(d[i-1] + 1, (flag1 * n + (d[int(i // 2)] + 1)), (flag2 * n + (d[int(i // 3)] + 1)))


print(d[n])