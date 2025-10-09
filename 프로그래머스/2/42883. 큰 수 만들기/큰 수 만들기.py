def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < int(num):
            stack.pop()
            k -= 1
        stack.append(int(num))

    if k > 0:
        stack = stack[:-k]

    return ''.join(map(str, stack))
