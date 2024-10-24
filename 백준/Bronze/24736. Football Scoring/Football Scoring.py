pt_list = []
for _ in range(2):
    t, f, s, p, c = map(int, input().split())
    pt_list.append(6*t + 3*f + 2*s + 1*p + 2*c)

for point in pt_list:
    print(point, end = " ")