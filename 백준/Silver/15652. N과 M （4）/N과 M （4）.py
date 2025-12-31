from itertools import combinations_with_replacement
N, M = map(int, input().split())
my_list = [int(i) for i in range(1, N + 1)]
for res in list(combinations_with_replacement(my_list, M)):
    print(*res)