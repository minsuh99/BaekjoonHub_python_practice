import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    temp = input().split()
    
    if temp[0] == "push":
        stack.append(int(temp[1]))
    elif temp[0] == "pop":
        print(stack.pop() if stack else -1)
    elif temp[0] == "size":
        print(len(stack))
    elif temp[0] == "empty":
        print(0 if stack else 1)
    elif temp[0] == "top":
        print(stack[-1] if stack else -1)
