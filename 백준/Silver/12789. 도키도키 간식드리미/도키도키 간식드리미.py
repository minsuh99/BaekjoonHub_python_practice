from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stack = deque(map(int, input().rstrip().split()))
stack2 = []
target_num = 1
answer = "Nice"

while stack or stack2:
    if stack and stack[0] == target_num:
        stack.popleft()
        target_num += 1
    elif stack2 and stack2[-1] == target_num:
            stack2.pop()
            target_num += 1
    elif stack:
        stack2.append(stack.popleft())
    else:
        answer = "Sad"
        break

print(answer)