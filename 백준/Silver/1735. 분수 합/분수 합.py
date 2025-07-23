a, b = map(int, input().split())
c, d = map(int, input().split())

up = a * d + b * c
down = b * d

gcd = 0
large = up if up > down else down
small = down if up > down else up
while True:
    (large, small) = (large, small) if large > small else (small, large)
    large %= small
    
    if large == 0:
        gcd = small
        break

print(up // gcd, down // gcd)