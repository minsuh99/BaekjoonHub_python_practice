n = int(input())

my_list = [0 for _ in range(12)]

my_list[1] = 1
my_list[2] = 2
my_list[3] = 4

for i in range(4, 12):
    my_list[i] = my_list[i - 3] + my_list[i - 2] + my_list[i - 1]

for _ in range(n):
    print(my_list[int(input())])