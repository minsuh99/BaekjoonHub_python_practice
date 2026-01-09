N = int(input())
num_list = set([int(i) for i in input().split()])
M = int(input())
check_num = [int(i) for i in input().split()]

for num in check_num:
    if num in num_list:
        print(1)
    else:
        print(0)