import math


n = int(input())
cnt = 0
for a in range(1, 501):
    if a ** 2 - n <= 0:
        continue
    if ((a ** 2 - n) ** 0.5) % 1 == 0:
        cnt += 1

print(cnt)