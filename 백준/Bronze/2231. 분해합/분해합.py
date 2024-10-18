n = int(input())
res = 0

for i in range(max(1, n-9*len(str(n))), n+1):
    decompose_sum = i + sum(map(int, str(i)))
    if decompose_sum == n:
        res = i
        break

print(res)