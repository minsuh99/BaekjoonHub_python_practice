A = list(input())
B = input().split()

res = []

for alpha in A:
    if alpha in B:
        res.append(alpha.lower())
    else:
        res.append(alpha)

print("".join(res))