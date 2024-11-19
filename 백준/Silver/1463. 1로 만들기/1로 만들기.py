my_list = [0] * 1000001

my_list[1] = 0
my_list[2] = 1
my_list[3] = 1

n = int(input())

for i in range(4, n + 1):
    num2 = 1000001
    num3 = 1000001
    num1 = my_list[i-1] + 1
    if i % 2 == 0:
        num2 = my_list[i // 2] + 1
    if i % 3 == 0:
        num3 = my_list[i // 3] + 1
    my_list[i] = min(min(num1, num2), num3)

print(my_list[n])