import sys
input = sys.stdin.readline
my_list = list(map(int, input().rstrip().split()))

asc_list = [int(i) for i in range(1, 9)]
desc_list = [int(i) for i in range(8, 0, -1)]

if my_list == asc_list:
    print("ascending")
elif my_list == desc_list:
    print("descending")
else:
    print("mixed")