fac_list = []

for i in range(11):
    if i == 0:
        fac_list.append(1)
    else:
        fac_list.append(fac_list[i-1] * i)

n, k = map(int, input().split())

print(fac_list[n] // (fac_list[k] * fac_list[n-k]))