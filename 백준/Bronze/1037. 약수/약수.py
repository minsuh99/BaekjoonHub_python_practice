import sys

input = sys.stdin.readline

n = int(input())
divisors = sorted(list(map(int, input().split())))

if n % 2 == 0:
    print(divisors[0] * divisors[-1])
else:
    print(divisors[n // 2] ** 2)

