def solution(s):
    answer = True
    
    stack = []
    
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack.pop() == ")":
                answer = False
                break
    
    if stack:
        answer = False
    

    return answer