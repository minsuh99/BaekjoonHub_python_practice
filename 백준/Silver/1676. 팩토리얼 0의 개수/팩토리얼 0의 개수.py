fac = [1 for _ in range(501)]
for i in range(1, 501):
    fac[i] = fac[i-1] * i

N = int(input())
res = 0

temp = fac[N]
while True:
    if temp % 10 == 0:
        res += 1
        temp //= 10
    else:
        break

print(res)