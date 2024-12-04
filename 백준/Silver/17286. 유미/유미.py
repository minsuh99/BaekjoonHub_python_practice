from itertools import permutations

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

origin = [int(i) for i in input().split()]
coor_list = [list(map(int, input().split())) for _ in range(3)]

min_distance = float('inf')
for perm in permutations(coor_list):
    total_distance = dist(origin, perm[0])
    for i in range(2):
        total_distance += dist(perm[i], perm[i + 1]) 
    min_distance = min(min_distance, total_distance)

print(int(min_distance))
