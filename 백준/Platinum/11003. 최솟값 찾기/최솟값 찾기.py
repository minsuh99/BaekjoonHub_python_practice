from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
num_list = list(map(int, input().split()))
deq = deque()

for i in range(N):
    if not deq:
        deq.append((i, num_list[i]))
    else:
        while deq and num_list[i] < deq[-1][1]:
            deq.pop()
        deq.append((i, num_list[i]))
    
    if deq[0][0] < i - L + 1:
        deq.popleft()
    
    print(deq[0][1], end=" ")
