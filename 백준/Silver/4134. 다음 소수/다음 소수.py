def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    x = n
    while True:
        if is_prime(x):
            print(x)
            break
        else:
            x += 1
    