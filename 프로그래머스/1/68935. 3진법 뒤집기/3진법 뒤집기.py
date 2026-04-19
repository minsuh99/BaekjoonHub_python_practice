def solution(n):
    answer = 0
    tri = ''
    max_p = 0
    while True:
        if n < 3 ** max_p:
            break
        max_p += 1
    max_p -= 1
    
    while max_p >= 0:
        tri += str(n // (3 ** max_p))
        n -= int(tri[-1]) * 3 ** max_p
        max_p -= 1
    
    for i, num in enumerate(tri):
        answer += int(num) * 3 ** i
    return answer