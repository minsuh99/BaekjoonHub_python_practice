import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    res = -1
    max_year = M * N // gcd(M, N)

    cur_year = x
    while cur_year <= max_year:
        if (cur_year - y) % N == 0:
            res = cur_year
            break
        else:
            cur_year += M
    print(res)