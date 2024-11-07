n, x = map(int, input().split())
my_list = [int(i) for i in input().split()]

for i in my_list:
    if i < x:
        print(i, end=" ")