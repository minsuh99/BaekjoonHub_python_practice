N = int(input())
res = ""

if N == 0:
    print(0)
    exit()

while N != 0:
    q, r = divmod(N, -2)
    if r < 0:
        q += 1
        r += 2
    res = str(r) + res
    N = q

print(res)
