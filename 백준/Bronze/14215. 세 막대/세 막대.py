import sys
input = sys.stdin.readline

a, b, c = map(int ,input().split())

if sum([a, b, c]) > max(a, b, c) * 2:
    print(a + b + c)
else:
    print(2 * (sum([a, b, c]) - max(a, b, c)) - 1)