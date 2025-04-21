n = int(input())
list1 = [int(i) for i in input().split()]

m = int(input())
list2 = [int(i) for i in input().split()]

my_dict = dict()

for num in list1:
    my_dict[num] = 1

list2 = [my_dict.get(num, 0) for num in list2]
print(*list2)