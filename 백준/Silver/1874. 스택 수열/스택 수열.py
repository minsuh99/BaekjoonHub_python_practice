import sys
input = sys.stdin.readline

N = int(input())
stack = []
res = []
cur_num = 0

for _ in range(N):
    temp = int(input())

    while cur_num < temp:
        cur_num += 1
        stack.append(cur_num)
        res.append("+")

    if stack and stack[-1] == temp:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        sys.exit(0)

for i in res:
    print(i)