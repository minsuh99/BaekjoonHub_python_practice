import sys

n = int(sys.stdin.readline())
my_list=[]
for _ in range(n):
    my_list.append(int(sys.stdin.readline()))

my_list.sort()

for num in my_list:
    print(num)