n, m = map(int, input().split())
num_list = [int(i) for i in input().split()]
res = []
temp = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            Sum = num_list[i]+num_list[j]+num_list[k]
            res.append(Sum)
final = [(i if i <= m else 0) for i in sorted(res)]
print(max(final))
