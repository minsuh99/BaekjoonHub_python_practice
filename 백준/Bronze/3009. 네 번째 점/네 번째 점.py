point_list = []
ans_list = []

max_x, max_y, min_x, min_y = 0, 0, 1001, 1001

for _ in range(3):
    a, b = map(int, input().split())
    point_list.append((a,b))
    max_x = max(a, max_x)
    max_y = max(b, max_y)
    min_x = min(a, min_x)
    min_y = min(b, min_y)

ans_list = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]

res = [i for i in ans_list if i not in point_list]
print(res[0][0], res[0][1])
