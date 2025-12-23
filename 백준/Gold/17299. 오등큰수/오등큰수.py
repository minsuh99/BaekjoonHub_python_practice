N = int(input())
my_list = [int(i) for i in input().split()]
count_list = [0 for _ in range(1000001)]
res_list = [-1 for _ in range(N)]

for num in my_list:
    count_list[num] += 1


stack = []

for i, num in enumerate(my_list):
    if stack:
        while True:
            if stack and stack[-1][1] < count_list[num]:
                idx, _ = stack.pop()
                res_list[idx] = num
            else:
                break

    stack.append((i, count_list[num]))

print(*res_list)