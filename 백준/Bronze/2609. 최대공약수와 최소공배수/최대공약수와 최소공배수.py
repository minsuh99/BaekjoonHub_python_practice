def gcd(a, b):
    res = 0
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            res = i
    return res


a, b = map(int, input().split())
print(gcd(a,b))
print(a*b//gcd(a,b))