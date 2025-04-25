n = int(input())

my_list = [0 for _ in range(101)]

my_list[1] = 1
my_list[2] = 1
my_list[3] = 1

for i in range(4, 101):
    my_list[i] = my_list[i - 3] + my_list[i - 2]

for _ in range(n):
    print(my_list[int(input())])