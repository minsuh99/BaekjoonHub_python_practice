import sys
input = sys.stdin.readline

N = int(input())
my_list = [0 for _ in range(10001)]

for _ in range(N):
    my_list[int(input())] += 1

for i in range(10001):
    for j in range(my_list[i]):
        print(i)