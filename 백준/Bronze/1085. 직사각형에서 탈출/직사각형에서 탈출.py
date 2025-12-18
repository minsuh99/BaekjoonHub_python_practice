x, y, w, h = map(int, input().split())

print(min(min(abs(x - w), x), min(abs(y - h), y)))