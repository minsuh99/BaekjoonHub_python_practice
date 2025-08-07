A, B = map(int, input().split())
x1 = int(A * (-1) - (A ** 2 - B) ** 0.5)
x2 = int(A * (-1) + (A ** 2 - B) ** 0.5)

if x1 == x2:
    print(x1)
else:
    print(x1, x2)