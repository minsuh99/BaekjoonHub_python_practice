import sys

while True:
    a, b = map(float, sys.stdin.readline().split())
    if a * b == 0:
        print("AXIS")
        if a == 0 and b == 0:
            break
        else:
            continue
    else:
        if a > 0:
            if b > 0:
                print("Q1")
            elif b < 0:
                print("Q4")
        elif a < 0:
            if b > 0:
                print("Q2")
            elif b < 0:
                print("Q3")