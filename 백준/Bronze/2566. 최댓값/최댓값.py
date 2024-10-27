num_mat = [[0]*9]*9
row, col = 0, 0
max_val = 0
for i in range(9):
    num_mat[i] = [int(i) for i in input().split()]

for i in range(9):
    if max(num_mat[i]) > max_val:
        max_val = max(num_mat[i])
        row, col = i, num_mat[i].index(max_val)

print(max_val)
print(row+1, col+1)