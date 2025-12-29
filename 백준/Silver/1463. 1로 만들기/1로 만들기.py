Max = 1000001
d = [0 for _ in range(Max)]
d[1] = 0
d[2] = 1
d[3] = 1

for i in range(4, Max):
    flag1 = (i % 2 != 0)
    flag2 = (i % 3 != 0)
    d[i] = min(d[i-1] + 1, (flag1 * Max + (d[int(i // 2)] + 1)), (flag2 * Max + (d[int(i // 3)] + 1)))

n = int(input())
print(d[n])