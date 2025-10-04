import sys
input = sys.stdin.readline

N = int(input())
prime_list = [int(i) for i in range(10000001)]
prime_list[0] = prime_list[1] = 0

for i in range(2, int(len(prime_list) ** 0.5) + 1):
    if prime_list[i] == 0:
        continue
    for j in range(2*i, len(prime_list), i):
        prime_list[j] = 0

for prime in prime_list:
    if prime >= N and str(prime) == str(prime)[::-1]:
        break

print(prime)