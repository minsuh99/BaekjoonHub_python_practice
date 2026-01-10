import sys
input = sys.stdin.readline

N, M = map(int, input().split())
my_dict = {}

for i in range(1, N + 1):
    name = input().rstrip()
    my_dict[i] = name
    my_dict[name] = i

for _ in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(my_dict[int(query)])
    else:
        print(my_dict[query])