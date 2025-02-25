from itertools import combinations
n, m = map(int, input().split())
for comp in list(combinations(range(1, n + 1), m)):
    print(" ".join(map(str, comp)))