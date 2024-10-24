import sys

n = int(sys.stdin.readline())
card_list = [int(i) for i in sys.stdin.readline().split()]

m = int(sys.stdin.readline())
num_list = [int(i) for i in sys.stdin.readline().split()]

res_dict = {}

for i in card_list:
    if i in res_dict:
        res_dict[i] += 1
    else:
        res_dict[i] = 1

for num in num_list:
    print(res_dict[num] if num in res_dict else 0, end = " ")