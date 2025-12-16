a, b, c = map(int, input().split())

temp1 = [a, b, c]
temp2 = set(temp1)

if len(temp1) == len(temp2):
    print(max(temp1) * 100)
else:
    if len(temp1) - len(temp2) == 1:
        print(1000 + (sum(temp1) - sum(temp2)) * 100)
    else:
        print(10000 + temp1[0] * 1000)