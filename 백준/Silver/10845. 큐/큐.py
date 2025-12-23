from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    oper = input().rstrip().split()
    if oper[0] == "push":
        queue.append(int(oper[1]))
    elif oper[0] == "pop":
        print(queue.popleft() if queue else -1)
    elif oper[0] == "size":
        print(len(queue))
    elif oper[0] == "empty":
        print(0 if queue else 1)
    elif oper[0] == "front":
        print(queue[0] if queue else -1)
    elif oper[0] == "back":
        print(queue[-1] if queue else -1)