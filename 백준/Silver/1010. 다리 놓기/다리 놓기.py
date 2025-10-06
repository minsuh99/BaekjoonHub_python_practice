import sys
input = sys.stdin.readline

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    if N < M:
        N, M = M, N
    
    print(factorial(N) // (factorial(M) * factorial(N - M)))