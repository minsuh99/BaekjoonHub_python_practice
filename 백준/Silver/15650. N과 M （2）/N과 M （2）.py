import sys
sys.setrecursionlimit(10**6)
from itertools import combinations
N, M = map(int, input().split())
my_list = [int(i) for i in range(1, N + 1)]
for res in list(combinations(my_list, M)):
    print(*res)