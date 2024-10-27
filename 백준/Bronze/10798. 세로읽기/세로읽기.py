my_list = []
max_len = 0
for i in range(5):
    my_list.append(input())
    if len(my_list[i]) > max_len:
        max_len = len(my_list[i])

for i in range(max_len):
    for j in range(5):
        if i+1 > len(my_list[j]):
            continue
        else:
            print(my_list[j][i], end="")