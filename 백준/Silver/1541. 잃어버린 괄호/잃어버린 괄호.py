import sys
input = sys.stdin.readline

equation = input().rstrip()
num_list = equation.split('-')
new_num = []
for nums in num_list:
    temp = list(map(int, nums.split('+')))
    new_num.append(sum(temp))

res = new_num[0]
for num in new_num[1:]:
    res -= num

print(res)