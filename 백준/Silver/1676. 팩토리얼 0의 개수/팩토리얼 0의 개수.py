n = int(input())
res = 1

for i in range(1, n+1):
    res *= i

res = str(res)[::-1]


if res.find('0') == -1:
    print(0)
else:
    for i in range(res.find('0')+1, len(res)+1):
        if res[i] != '0':
            print(i)
            break