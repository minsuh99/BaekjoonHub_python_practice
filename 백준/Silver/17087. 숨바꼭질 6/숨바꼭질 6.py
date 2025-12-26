import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, S = map(int, input().split())
my_list = [abs(int(i) - S) for i in input().split()]
res = my_list[0]

if N != 1:
    for num in my_list[1:]:
        res = gcd(res, num)
print(res)