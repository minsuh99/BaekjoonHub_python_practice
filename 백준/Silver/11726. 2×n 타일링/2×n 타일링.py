n = int(input())

my_list = [0 for _ in range(1001)]

my_list[0] = 1
my_list[1] = 1

for i in range(2, 1001):
    my_list[i] = my_list[i - 2] + my_list[i - 1]

print(my_list[n] % 10007)