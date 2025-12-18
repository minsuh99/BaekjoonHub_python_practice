N = int(input())
coord_x, coord_y = [], []

for _ in range(N):
    x, y = map(int, input().split())
    coord_x.append(x)
    coord_y.append(y)

print((max(coord_x) - min(coord_x)) * (max(coord_y) - min(coord_y)))