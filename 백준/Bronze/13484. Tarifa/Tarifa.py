X = int(input())
N = int(input())

can_spent = X

for _ in range(N):
    temp = int(input())
    left_mem = can_spent - temp
    if left_mem > 0:
        can_spent = X + left_mem
    else:
        can_spent = X

print(can_spent)