res = 0
idx = 0
for i in range(1,10):
    num = int(input())
    if num > res:
        res = num
        idx = i

print(res)
print(idx)