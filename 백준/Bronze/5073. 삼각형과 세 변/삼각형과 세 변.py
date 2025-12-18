import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        exit()
    
    if sum([a, b, c]) <= max(a, b, c) * 2:
        print("Invalid")
    else:    
        if a == b == c:
            print("Equilateral")
        elif (a == b and b != c) or (a == c and b != a) or (b == c and c != a):
            print("Isosceles")
        else:
            print("Scalene")