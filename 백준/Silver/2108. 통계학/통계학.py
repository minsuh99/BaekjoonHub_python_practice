import sys

n = int(sys.stdin.readline())
num_list=[]
cnt_dict = {}
max_count_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

for i in num_list:
    if i in cnt_dict:
        cnt_dict[i] += 1
    else:
        cnt_dict[i] = 1

for i in cnt_dict:
    if cnt_dict[i] == max(cnt_dict.values()):
        max_count_list.append(i)

print(int(round(sum(num_list) / len(num_list), 0)))
print(num_list[(len(num_list)-1) // 2])
print(max_count_list[0] if len(max_count_list) == 1 else max_count_list[1])
print(max(num_list)-min(num_list))