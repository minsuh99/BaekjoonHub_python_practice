n = int(input())
res = 0
for i in range(1, n+1):
    decompose_sum = i + sum(map(int, str(i)))
    if decompose_sum == n:
        res = i
        break

print(res)