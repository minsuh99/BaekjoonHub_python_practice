import sys
input = sys.stdin.readline

A, B = map(int, input().split())
num_list = [int(i) for i in range(int(B ** 0.5) + 1)]
num_list[0] = num_list[1] = 0

for i in range(2, int(int(B ** 0.5)**0.5) + 1):
    if num_list[i] == 0:
        continue
    
    for j in range(2*i, int(B ** 0.5)+1, i):
        num_list[j] = 0

prime_list = [i for i in num_list if i > 0 and i <= int(B ** 0.5)]
cnt = 0

for prime in prime_list:
    temp = prime * prime
    while temp <= B:
        if temp >= A:
            cnt += 1
        if temp > B // prime:
            break
        temp *= prime

print(cnt)