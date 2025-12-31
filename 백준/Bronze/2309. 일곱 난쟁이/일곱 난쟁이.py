height = []
for _ in range(9):
    height.append(int(input()))

total = sum(height)
res = []

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        
        if total - height[i] - height[j] == 100:
            res = [height[k] for k in range(9) if k != i and k != j]
            break
    if res:
        res.sort()
        break

for h in res:
    print(h)