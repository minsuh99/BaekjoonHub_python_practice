from itertools import permutations
N, M = map(int, input().split())
my_list = [int(i) for i in range(1, N + 1)]
for ans in list(permutations(my_list, M)):
    print(*ans)