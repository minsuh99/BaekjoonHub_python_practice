from itertools import permutations

n, m = map(int, input().split())
for comp in list(permutations(range(1, n + 1), m)):
    print(" ".join(map(str, comp)))