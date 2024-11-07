a, b = map(int, input().split())
a, b = int(str(a)[::-1]), int(str(b)[::-1])

if a>b:
    print(a)
else:
    print(b)