l, p = map(int, input().split())
my_list = [int(i) for i in input().split()]

for i in range(5):
    print(my_list[i] - l*p , end=" ")