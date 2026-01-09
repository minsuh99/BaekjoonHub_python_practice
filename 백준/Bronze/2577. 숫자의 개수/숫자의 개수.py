A = int(input())
B = int(input())
C = int(input())

num = str(A*B*C)
res = [0 for _ in range(10)]

for n in num:
    res[int(n)] += 1

for i in res:
    print(i)
