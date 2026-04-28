def solution(order):
    box = [i for i in range(len(order), 0, -1)]
    stack = []
    idx = 0
    while idx != len(order):
        if stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
        elif box:
            stack.append(box.pop())
        else:
            return idx
    
    return idx