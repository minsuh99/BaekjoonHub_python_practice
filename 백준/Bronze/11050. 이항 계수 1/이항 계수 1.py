fac = [1 for _ in range(11)]
for i in range(1, 11):
    fac[i] = fac[i - 1] * i

N, K = map(int, input().split())
print(fac[N] // (fac[K] * fac[N - K]))