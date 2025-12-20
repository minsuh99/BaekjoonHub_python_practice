import sys
input = sys.stdin.readline

my_list = []

N = int(input())

for i in range(N):
    age, name = map(str, input().split())
    my_list.append((int(age), name, i))

my_list.sort(key=lambda x:((x[0], x[2])))

for age, name, _ in my_list:
    print(age, name)