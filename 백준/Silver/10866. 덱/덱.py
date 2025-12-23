from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque()

for _ in range(N):
    oper = input().rstrip().split()
    if oper[0] == "push_front":
        deq.appendleft(int(oper[1]))
    elif oper[0] == "push_back":
        deq.append(int(oper[1]))
    elif oper[0] == "pop_front":
        print(deq.popleft() if deq else -1)
    elif oper[0] == "pop_back":
        print(deq.pop() if deq else -1)
    elif oper[0] == "size":
        print(len(deq))
    elif oper[0] == "empty":
        print(0 if deq else 1)
    elif oper[0] == "front":
        print(deq[0] if deq else -1)
    elif oper[0] == "back":
        print(deq[-1] if deq else -1)