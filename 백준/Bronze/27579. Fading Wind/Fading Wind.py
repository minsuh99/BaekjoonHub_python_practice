import math

h, k, v, s = map(int, input().split())
res = 0

while h > 0:
    v += s
    v -= max(1, math.floor(v/10))
    if v >= k:
        h += 1
    elif v > 0:
        h -= 1
        if h == 0:
            v = 0
    else:
        h = 0
        v = 0
    res += v
    
    if s > 0:
        s -= 1

print(res)