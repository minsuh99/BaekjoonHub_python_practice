import sys

n = int(sys.stdin.readline())
my_list = [int(i) for i in sys.stdin.readline().split()]
sorted_list = sorted(set(my_list))
my_dict = dict()

for i, num in enumerate(sorted_list):
    my_dict[num] = i

my_list = [my_dict[num] for num in my_list]

# for num in my_list:
#    print(num, end=" ")

print(*my_list)