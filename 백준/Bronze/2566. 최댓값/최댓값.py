num_list = [[int(i) for i in input().split()] for _ in range(9)]
max_val = max([i for j in range(9) for i in num_list[j]])
max_flag = False

for i in range(9):
    for j in range(9):
        if num_list[i][j] == max_val:
            max_flag = True
            break
    if max_flag:
        break

print(max_val)
print(i+1, j+1)