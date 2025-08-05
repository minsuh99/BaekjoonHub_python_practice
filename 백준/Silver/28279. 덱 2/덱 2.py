from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
my_deq = deque()

for _ in range(N):
    command = input().rstrip().split()
    match int(command[0]):
        case 1:
            my_deq.appendleft(int(command[1]))
        case 2:
            my_deq.append(int(command[1]))
        case 3:
            if my_deq:
                print(my_deq.popleft())
            else:
                print(-1)
        case 4:
            if my_deq:
                print(my_deq.pop())
            else:
                print(-1)
        case 5:
            print(len(my_deq))
        case 6:
            if my_deq:
                print(0)
            else:
                print(1)
        case 7:
            if my_deq:
                print(my_deq[0])
            else:
                print(-1)
        case 8:
            if my_deq:
                print(my_deq[-1])
            else:
                print(-1)