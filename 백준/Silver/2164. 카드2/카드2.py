import sys

N = int(sys.stdin.readline())
num_list = [int(i) for i in range(1, N+1)]

while len(num_list) > 1:
    if len(num_list) % 2 == 0:
        num_list = num_list[1::2]
    else:
        num_list = num_list[1::2]
        temp = num_list.pop(0)
        num_list.insert(len(num_list), temp)

print(num_list[0])