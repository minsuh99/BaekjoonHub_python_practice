import sys
input = sys.stdin.readline

N = int(input())
my_list = []

for _ in range(N):
    my_list.append(int(input()))

for i in range(len(my_list) - 1):
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

for num in my_list:
    print(num)