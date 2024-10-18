import sys

num_list = list(range(1, 31))
num_list2 = []
for _ in range(28):
    num_list2.append(int(sys.stdin.readline().rstrip()))

final = sorted(list(set(num_list)-set(num_list2)))

for num in final:
    print(num)