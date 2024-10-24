import sys

k = int(sys.stdin.readline().rstrip())
num_list = []
for _ in range(k):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop()
print(sum(num_list))