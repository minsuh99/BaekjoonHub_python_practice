import sys
input = sys.stdin.readline

N = int(input())
my_list = [int(i) for i in input().split()]
res_list = [-1 for _ in range(N)]
stack = []

for i, num in enumerate(my_list):
    while stack and my_list[stack[-1][0]] < my_list[i]:
        idx, _ = stack.pop()
        res_list[idx] = my_list[i]
    stack.append((i, num))

for num in res_list:
    print(num, end=" ")