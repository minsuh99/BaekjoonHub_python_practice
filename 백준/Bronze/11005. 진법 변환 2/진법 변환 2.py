N, B = map(int, input().split())

if N == 0:
    print(0)
    exit()

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = []

while N > 0:
    res.append(digits[N % B])
    N //= B

print("".join(reversed(res)))
