import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(n*(n+1) // 2)