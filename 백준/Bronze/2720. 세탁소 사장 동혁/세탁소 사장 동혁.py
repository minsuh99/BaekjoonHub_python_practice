def cal_change(x):
    current = [25, 10, 5, 1]
    temp = []
    for cur in current:
        temp.append(x // cur)
        x %= cur
    
    return temp



T = int(input())

for _ in range(T):
    money = int(input())
    res = cal_change(money)
    
    for i in res:
        print(i, end=" ")
    print()