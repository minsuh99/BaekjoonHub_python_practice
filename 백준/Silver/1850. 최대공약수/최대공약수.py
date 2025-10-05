import sys
input = sys.stdin.readline

def gcd(a, b):    
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

A, B = map(int, input().split())
print("1"*gcd(A, B))
