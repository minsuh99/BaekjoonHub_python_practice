def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

M = int(input())
N = int(input())

prime_list = [i for i in range(M, N + 1) if is_prime(i)]

if prime_list:
    print(sum(prime_list))
    print(prime_list[0])
else:
    print(-1)