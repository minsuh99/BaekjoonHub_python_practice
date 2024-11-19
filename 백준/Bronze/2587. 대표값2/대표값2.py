my_list = []
for _ in range(5):
    my_list.append(int(input()))

print(sum(my_list) // len(my_list))
print(sorted(my_list)[2])