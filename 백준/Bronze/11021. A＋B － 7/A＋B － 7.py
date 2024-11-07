import sys

T = int(sys.stdin.readline())

for i in range(T):
    res = sum([int(i) for i in sys.stdin.readline().split()])
    print(f"Case #{i+1}: {res}")