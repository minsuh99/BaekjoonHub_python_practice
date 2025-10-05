import sys
input = sys.stdin.readline

N = int(input())
result = N

for prime in range(2, int(N ** 0.5) + 1):
    if N % prime == 0:
        result -= result // prime
        while N % prime == 0:
            N //= prime

if N > 1:
    result -= result // N

print(result)