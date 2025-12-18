import sys
input = sys.stdin.readline
N = int(input())

min_search = int(10**(len(str(N)) - 2))*9
res = 0

for num in range(min_search, N):
    temp = [int(i) for i in str(num)]
    if num + sum(temp) == N:
        res = num
        break
print(res)