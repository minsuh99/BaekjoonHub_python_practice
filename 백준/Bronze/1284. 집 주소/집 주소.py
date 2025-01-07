import sys

while True:
    n = int(sys.stdin.readline().strip())
    res = 0
    if n == 0:
        break
    for s in str(n):
        if s == '1':
            res += 2
        elif s == '0':
            res += 4
        else:
            res += 3
    res += len(str(n)) + 1
    print(res)