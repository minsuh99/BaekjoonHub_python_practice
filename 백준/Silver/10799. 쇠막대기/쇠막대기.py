batch = input()
stack = []

cur_stick = 0
res = 0
left_flag = False

for b in batch:
    if b == "(":
        stack.append(b)
        if left_flag:
            cur_stick += 1
        else:
            left_flag = True
    elif b == ")":
        stack.pop()
        if left_flag:
            res += cur_stick
        else:
            cur_stick -= 1
            res += 1
        left_flag = False

print(res)