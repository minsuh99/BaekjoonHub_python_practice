import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        exit()
    max_side = max([a, b, c])
    left = 0
    right = 0
    for side in [a, b, c]:
        if side != max_side:
            left += side ** 2
        else:
            right += side ** 2
    
    if left == right:
        print("right")
    else:
        print("wrong")