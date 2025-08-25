import sys

input = sys.stdin.readline

f = [0 for _ in range(41)]
f[1] = 1
f[2] = 1

n = int(input())

cnt = 0
for i in range(3, n + 1):
    cnt += 1
    f[i] = f[i - 1] + f[i - 2]


print(f[n], cnt)