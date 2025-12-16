import sys
input = sys.stdin.readlines

a = input()
for line in a:
    a, b = map(int, line.split())
    print(a+b)