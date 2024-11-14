n, w, h, l = map(int, input().split())
max_w = w // l
max_h = h // l
print(min(n, max_w * max_h))