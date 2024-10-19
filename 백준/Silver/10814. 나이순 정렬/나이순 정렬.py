import sys

N = int(sys.stdin.readline())
my_list = [sys.stdin.readline().split() for _ in range(N)]
for i in range(len(my_list)):
    my_list[i][0] = int(my_list[i][0])

new_list = sorted(my_list, key = lambda x:x[0])

for i in range(len(new_list)):
    print(new_list[i][0], new_list[i][1])