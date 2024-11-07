n = int(input())
order_list = [int(i) for i in input().split()]
res = []

for i in range(n):
    res.insert(i - order_list[i], i + 1)

for i in res:
    print(i, end=" ")