points = set()
must_points = set()

for _ in range(3):
    x, y = map(int, input().split())
    points.add((x, y))

coord_x = set([point[0] for point in points])
coord_y = set([point[1] for point in points])

for x in coord_x:
    for y in coord_y:
        must_points.add((x, y))

res = list(must_points - points)
print(list(*res)[0], list(*res)[1])