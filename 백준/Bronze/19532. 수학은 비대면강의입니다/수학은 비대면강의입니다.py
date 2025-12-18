a, b, c, d, e, f = map(int, input().split())

if b != 0:
    x = (f - c*e/b) / (d - a*e/b)
    y = (c - a*x) / b
else:
    x = c / a
    y = (f - d*x) / e
print(round(x), round(y))