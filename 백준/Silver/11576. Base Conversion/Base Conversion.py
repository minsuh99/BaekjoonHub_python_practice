import sys
input = sys.stdin.readline

A, B = map(int, input().split())
m = int(input())
A_num = [int(i) for i in input().split()]
B_num = []
dec_num = 0

for i in range(m):
    dec_num += A_num[i] * pow(A, m - i - 1)
    
while dec_num != 0:
    q, r = divmod(dec_num, B)
    B_num = [r] + B_num
    dec_num = q

print(*B_num)
    