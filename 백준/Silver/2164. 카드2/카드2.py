import sys

N = int(sys.stdin.readline())
num_list = [int(i) for i in range(1, N+1)]

while len(num_list) > 1:
    if len(num_list) % 2 == 0:
        num_list = num_list[1::2]
    else:
        num_list = num_list[1::2]
        temp = num_list.pop(0)
        num_list.insert(len(num_list), temp)

print(num_list[0])

# 84ms
# 너무 수학적임

from collections import deque

N = int(sys.stdin.readline())
card = deque([i for i in range(1, N+1)])

while len(card) > 1:
    card.popleft()
    card.rotate(-1)

print(card[0])

# 180ms
# 오히려 이게 더 메모리를 잡아먹고 시간도 좀 걸리는듯.. 왜지
# popleft: 가장 왼쪽의 요소를 pop
# rotate: 왼쪽으로 한 칸 회전 2 3 4 -> 3 4 2
