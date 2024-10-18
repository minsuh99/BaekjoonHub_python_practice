my_list = []

for _ in range(10):
    num = int(input())
    my_list.append(num%42)

print(len(set(my_list)))