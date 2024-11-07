import math

a, b, c, d, e, f = map(int, input().split())

if b != 0:
    x = (b*f- c*e) // (b*d - a*e)
    y = (c - a * x) // b

else:
    x = c // a
    y = (f - d * x) // e

print(x, y)