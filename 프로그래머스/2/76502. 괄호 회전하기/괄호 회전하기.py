from collections import deque


def check_s(sentence):
    stack = []
    
    for s in sentence:
        if s in ["(", "[", "{"]:
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif s == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
    if stack:
        return False
    
    return True

def solution(s):
    answer = 0
    s = deque(s)
    
    for _ in range(len(s)):
        s.rotate(1)
        answer += check_s(s)
    
    
    return answer