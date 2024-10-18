import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==0 & b==0 & c==0:
        break
    num_list = sorted([a, b, c])
    if num_list[0]**2 + num_list[1]**2 == num_list[2]**2:
        print("right")
    else:
        print("wrong")