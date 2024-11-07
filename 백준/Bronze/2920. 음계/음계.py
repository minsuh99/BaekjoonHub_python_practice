my_list = [int(i) for i in input().split()]
asc_list = sorted(my_list)
desc_list = sorted(my_list, reverse=True)

if my_list == asc_list:
    print("ascending")
elif my_list == desc_list:
    print("descending")
else:
    print("mixed")