n = int(input())

row_dot = 2

for i in range(n):
    row_dot += row_dot - 1

print(row_dot ** 2)
