from collections import deque
import sys
input = sys.stdin.readline

word = input().rstrip()

cur_left = deque(list(word))
cur_right = deque()

M = int(input())

for _ in range(M):
    temp = input().split()
    
    if temp[0] == "L":
        if cur_left:
            cur_right.appendleft(cur_left.pop())

    elif temp[0] == "D":
        if cur_right:
            cur_left.append(cur_right.popleft())
    elif temp[0] == "B":
        if cur_left:
            cur_left.pop()
    elif temp[0] == "P":
        cur_left.append(temp[1])

print("".join(list(cur_left) +  list(cur_right)))