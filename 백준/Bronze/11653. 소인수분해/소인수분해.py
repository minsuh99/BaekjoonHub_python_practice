def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

N = int(input())
num = 2
while num * num <= N:
    while N % num == 0:
        print(num)
        N //= num
    num += 1

if N > 1:
    print(N)