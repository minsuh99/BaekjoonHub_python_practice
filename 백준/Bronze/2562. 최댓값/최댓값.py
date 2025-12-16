max_val = 0
max_idx = 0

for i in range(9):
    val = int(input())
    if val > max_val:
        max_val = val
        max_idx = i + 1

print(max_val)
print(max_idx)