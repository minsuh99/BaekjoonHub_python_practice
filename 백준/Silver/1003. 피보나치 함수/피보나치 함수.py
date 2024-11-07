fibo_list = [0, 1]
for i in range(40):
    fibo_list.append(fibo_list[i] + fibo_list[i+1])

T = int(input())

for _ in range(T):
    num = int(input())
    if num == 0:
        print(1, 0)
    else:
        print(fibo_list[num - 1], fibo_list[num])