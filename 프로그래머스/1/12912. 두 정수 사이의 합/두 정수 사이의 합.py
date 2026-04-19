def solution(a, b):
    a, b = (b, a) if b < a else (a, b)
    answer = sum(range(a, b + 1))
    return answer