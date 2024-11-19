n, k = map(int, input().split())
my_list = [int(i) for i in input().split()]

my_list.sort(reverse=True)

print(my_list[k-1])