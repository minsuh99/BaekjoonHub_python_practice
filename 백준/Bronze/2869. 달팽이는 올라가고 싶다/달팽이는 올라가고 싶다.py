A, B, V = map(int, input().split())
res = 0

res += (V - A) // (A - B)
if (V - A) % (A - B) != 0:
    print(res + 2)
else:
    print(res + 1)
