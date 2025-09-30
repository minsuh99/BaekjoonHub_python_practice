import sys
input = sys.stdin.readline

N = int(input())
my_list = []

for i in range(N):
    my_list.append((i, int(input())))

my_list.sort(key=lambda x:x[1])
max = 0
for i in range(len(my_list)):
    if max < my_list[i][0] - i:
        max = my_list[i][0] - i

print(max + 1) # swap이 일어나지 않는 반복문도 한 번 돌기 때문에