a, b = map(int, input().split())
answer = a * b

large = a if a > b else b
small = b if a > b else a
while True:
    (large, small) = (large, small) if large > small else (small, large)
    large %= small
    
    if large == 0:
        answer //= small
        break

print(answer)