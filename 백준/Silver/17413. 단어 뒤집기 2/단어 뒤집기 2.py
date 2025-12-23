from collections import deque
import sys
input = sys.stdin.readline

S = input().rstrip()
queue = deque()
res = ""
flag = False

def return_str(queue, word):
    while queue:
        word += queue.popleft()
    
    return word

for s in S:
    if s == "<":
        queue.append(s)
        flag = True
    elif s == ">":
        queue.append(s)
        flag = False
        res = return_str(queue, res)
    elif s == " ":
        queue.append(s)
        if "<" in queue:
            pass
        else:
            res = return_str(queue, res)
    else:
        if flag:
            queue.append(s)
        else:
            queue.appendleft(s)

if queue:
    res = return_str(queue, res)

print(res)