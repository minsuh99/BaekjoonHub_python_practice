from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
my_deq = deque(range(1, N+1))
balloon_num = [0] + [int(i) for i in input().rstrip().split()]
res = []

while my_deq:
    idx = my_deq[0]
    rotate_num = balloon_num[idx]
    res.append(idx)
    my_deq.popleft()
    
    if not my_deq:
        break
    
    if rotate_num > 0:
        my_deq.rotate((rotate_num - 1) * (-1))
    else:
        my_deq.rotate(rotate_num * (-1))

print(*res)