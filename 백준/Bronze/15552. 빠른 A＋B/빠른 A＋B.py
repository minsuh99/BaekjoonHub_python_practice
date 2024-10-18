import sys

T = int(sys.stdin.readline())

for _ in range(T):
    print(sum([int(i) for i in sys.stdin.readline().split()]))