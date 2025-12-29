import sys
input = sys.stdin.readline

T = int(input())

prime_list = [True] * (1000001)
prime_list[0] = False
prime_list[1] = False

for i in range(2, 1001):
    if prime_list[i]:
        for j in range(i * i, 1000001, i):
            prime_list[j] = False

for _ in range(T):
    res = 0
    num = int(input())
    
    if num >= 4 and prime_list[2] and prime_list[num - 2]:
        res += 1
    
    for n in range(3, num // 2 + 1, 2):
        if prime_list[n] and prime_list[num - n]:
            res += 1
    
    print(res)
