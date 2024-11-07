def is_prime(n:int):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False



n = int(input())
num_list = [int(i) for i in input().split()]
print(sum([is_prime(i) for i in num_list]))