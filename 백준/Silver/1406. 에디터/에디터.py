import sys
from collections import deque

base_word = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
attach_word = deque()

for _ in range(M):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "L" and base_word:
        attach_word.appendleft(base_word.pop())
    elif command[0] == "D" and attach_word:
        base_word.append(attach_word.popleft())
    elif command[0] == "B" and base_word:
        base_word.pop()
    elif command[0] == "P":
        base_word.append(command[1])

final_word = base_word + list(attach_word)
print("".join(final_word))