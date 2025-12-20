import sys
input = sys.stdin.readline

my_list = []

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    my_list.append((x, y))

my_list.sort(key=lambda x:((x[1], x[0])))

for coord in my_list:
    print(coord[0], coord[1])