import sys
input = sys.stdin.readline

my_str = input().rstrip().split("-")
res = 0

for i in range(len(my_str)):
    my_str[i] = [int(j) for j in my_str[i].split("+")]
    if i == 0:
        res += sum(my_str[i])
    else:
        res -= sum(my_str[i])

print(res)