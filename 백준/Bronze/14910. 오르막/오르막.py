def descend(ls1:list, ls2:list):
    if ls1 == ls2:
        return "Good"
    return "Bad"

my_list = [int(i) for i in input().split()]
my_list2 = sorted(my_list)
print(descend(my_list, my_list2))