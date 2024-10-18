def decompose_sum(n: int):
    return n + sum([int(i) for i in str(n)])
    

n = int(input())
res = 0
for i in range(n):
    if decompose_sum(i) == n:
        res = i
        break
print(res)