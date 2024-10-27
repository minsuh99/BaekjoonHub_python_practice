m, n = map(int, input().split())

num_list = [False, False] + [True] * (n-1)
res_list = []

for i in range(2, n+1):
    if num_list[i]:
        res_list.append(i)
        for j in range(2*i, n+1, i):
            num_list[j] = False

res_list = [i for i in res_list if i >= m]

for num in res_list:
    print(num)