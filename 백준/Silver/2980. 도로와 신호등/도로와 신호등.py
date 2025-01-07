N, L = map(int, input().split())

road = [0 for _ in range(L + 1)]

for _ in range(N):
    D, R, G = map(int, input().split())
    road[D] = [R, G]

t = 0
pos = 0

while pos < L:
    if road[pos] == 0:
        pos += 1
    else:
        R, G = road[pos]
        if (t % (R + G)) < R:
            pass
        else:
            pos += 1
    t += 1
print(t)