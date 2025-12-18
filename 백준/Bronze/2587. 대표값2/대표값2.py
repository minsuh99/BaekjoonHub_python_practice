import sys
input = sys.stdin.readline

my_list = []

for _ in range(5):
    my_list.append(int(input()))

for i in range(len(my_list) - 1):
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

print(sum(my_list) // len(my_list))
print(my_list[2])