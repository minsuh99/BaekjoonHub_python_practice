def solution(s):
    answer = True
    stack = []    
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True