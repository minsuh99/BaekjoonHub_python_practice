n = int(input())
time_list = sorted([int(i) for i in input().split()])
res = 0

for i in range(len(time_list)):
    res += sum(time_list[:i+1])

print(res)