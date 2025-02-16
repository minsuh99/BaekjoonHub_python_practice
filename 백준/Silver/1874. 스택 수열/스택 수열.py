import sys

n = int(sys.stdin.readline())
my_list = []
for _ in range(n):
    my_list.append(int(sys.stdin.readline()))

temp = [i for i in range(1, n+1)]
stack = []
res = []

cur_idx = 0

while cur_idx < n:
    if stack and stack[-1] == my_list[cur_idx]:
        res.append("-")
        stack.pop()
        cur_idx += 1
    elif temp and temp[0] <= my_list[cur_idx]:
        res.append("+")
        stack.append(temp.pop(0))
    else:
        print("NO")
        sys.exit(0)
        
print("\n".join(res))
