def solution(s):
    answer = -1
    stack = []
    
    for char in s:
        if not stack or char not in stack:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
                
    return answer