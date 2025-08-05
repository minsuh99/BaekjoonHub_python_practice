from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
M = int(input())
C = list(map(int, input().rstrip().split()))

temp = deque()
res = []

for i, a in enumerate(A):
    if A[i] == 0:
        temp.append(B[i])

for num in C:
    temp.appendleft(num)
    res.append(temp.pop())

print(*res)