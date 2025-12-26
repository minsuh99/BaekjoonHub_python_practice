def gcd(a, b):
    if a == 0:
        return b
    else:
        x, y = max(a, b), min(a, b)
        return gcd(x % y, y)
    
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A*B // gcd(A, B))