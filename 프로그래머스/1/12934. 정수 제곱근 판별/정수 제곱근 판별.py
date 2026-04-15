def solution(n):
    answer = 0
    x = int(n ** 0.5)
    if n ** 0.5 - x == 0:
        answer = (x + 1) ** 2
    else:
        answer = -1
    return answer