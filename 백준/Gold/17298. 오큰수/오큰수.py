N = int(input())
my_list = [int(i) for i in input().split()]
res_list = [-1 for _ in range(N)]

stack = []

for i, num in enumerate(my_list):
    if stack:
        while True:
            if stack and stack[-1][1] < num:
                idx, _ = stack.pop()
                res_list[idx] = num
            else:
                break

    stack.append((i, num))

print(*res_list)