n = int(input())
if n == 1:
    a, b = map(int, input().split())
    print(0)
else:
    max_x, max_y, min_x, min_y = -10000, -10000, 10000, 10000
    for _ in range(n):
        a, b = map(int, input().split())
        max_x = max(a, max_x)
        max_y = max(b, max_y)
        min_x = min(a, min_x)
        min_y = min(b, min_y)

    print((max_x - min_x) * (max_y - min_y))
