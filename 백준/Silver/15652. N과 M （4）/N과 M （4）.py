from itertools import combinations_with_replacement
n, m = map(int, input().split())
for comp in combinations_with_replacement(range(1, n+1), r=m):
    print(" ".join(map(str, comp)))