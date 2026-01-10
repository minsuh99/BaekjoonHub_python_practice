import math
n = int(input())

squares = [i*i for i in range(1, int(math.isqrt(n)) + 1)]

if n in squares:
    print(1)
    exit()

for a in squares:
    if n - a in squares:
        print(2)
        exit()

for a in squares:
    for b in squares:
        s = a + b
        if s > n:
            break
        if n - s in squares:
            print(3)
            exit()

print(4)
