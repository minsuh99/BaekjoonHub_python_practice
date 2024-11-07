def is_prime(x):
    num_list = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            num_list.add(i)
            num_list.add(x // i)
    
    if len(num_list) == 2:
        return True
    else:
        return False

m = int(input())
n = int(input())

res = []

for num in range(m, n+1):
    if is_prime(num):
        res.append(num)

if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))