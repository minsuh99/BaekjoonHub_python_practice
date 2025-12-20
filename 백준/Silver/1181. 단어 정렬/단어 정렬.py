import sys
input = sys.stdin.readline

N = int(input())
my_list = []

for _ in range(N):
    my_list.append(input().rstrip())

my_list = list(set(my_list))
my_list.sort(key=lambda x:(len(x), x))

for word in my_list:
    print(word)