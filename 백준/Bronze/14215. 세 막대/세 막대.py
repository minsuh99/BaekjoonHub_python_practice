len_list = sorted([int(i) for i in input().split()])

if len_list[2] >= len_list[0] + len_list[1]:
    len_list.pop()
    len_list.append(len_list[0] + len_list[1] - 1)

print(sum(len_list))