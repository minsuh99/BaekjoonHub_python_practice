fac = [1 for _ in range(1011)]
for i in range(1, 1011):
    fac[i] = fac[i - 1] * i

N = int(input())
print(fac[9 + N] // (fac[9] * fac[N]) % 10007)