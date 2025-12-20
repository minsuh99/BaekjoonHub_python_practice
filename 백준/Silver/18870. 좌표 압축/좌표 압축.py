import sys
input = sys.stdin.readline

N = int(input())
my_list = [int(i) for i in input().split()]

my_list2 = list(set(my_list.copy()))
my_list2.sort()

my_dict = {}

for i, num in enumerate(my_list2):
    my_dict[num] = i

for num in my_list:
    print(my_dict[num], end=" ")