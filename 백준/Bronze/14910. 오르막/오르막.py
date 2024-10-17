my_list = [int(i) for i in input().split()]
res = "Good"

for i in range(len(my_list)-1):
    if my_list[i] > my_list[i+1]:
        res = "Bad"
        break

print(res)