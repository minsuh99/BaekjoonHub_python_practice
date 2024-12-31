fibo_list = [1, 1]

n = int(input())

for i in range(n-2):
    fibo_list.append(fibo_list[i]+fibo_list[i+1])

print(fibo_list[-1])