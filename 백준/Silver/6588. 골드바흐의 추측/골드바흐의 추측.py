# def is_prime(n):
#     if n == 1:
#         return False

#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
        
#     return True
import sys
input = sys.stdin.readline


prime_list = [True] * (1000001)
prime_list[0] = False
prime_list[1] = False

for i in range(2, 1001):
    if prime_list[i]:
        for j in range(i * i, 1000001, i):
            prime_list[j] = False


while True:
    num = int(input())
    if num == 0:
        exit()
    flag = False
    
    
    for n in range(3, num // 2 + 1, 2):
        if prime_list[n] and prime_list[num - n]:
                print(f"{num} = {n} + {num - n}")
                flag = True
                break
            
    if not flag:
        print("Goldbach's conjecture is wrong.")
