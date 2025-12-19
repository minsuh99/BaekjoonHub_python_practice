import sys
input = sys.stdin.readline

N = int(input())
my_list = []

for _ in range(N):
    my_list.append(int(input()))

my_list.sort()

for num in my_list:
    print(num)