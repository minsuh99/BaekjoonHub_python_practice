import sys
input = sys.stdin.readline

while True:
    my_input = input().rstrip()
    if my_input == ".":
        exit()
    stack = []
    flag = True
    
    for s in my_input:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    if stack:
        flag = False
    
    print("yes" if flag else "no")