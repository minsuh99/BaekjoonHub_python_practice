def gcd(a, b):
    if a == 0:
        return b
    else:
        x, y = max(a, b), min(a, b)
        return gcd(x % y, y)

A, B = map(int, input().split())
G = gcd(A, B)
print(G)
print(A*B//G)
