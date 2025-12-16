N = int(input())
my_list = list(map(int, input().split()))
v = int(input())
res = 0

if v in my_list:
    for num in my_list:
        if num == v:
            res += 1

print(res)