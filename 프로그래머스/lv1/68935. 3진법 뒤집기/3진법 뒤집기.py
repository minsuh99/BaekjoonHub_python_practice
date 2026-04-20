def solution(n):
    answer = 0
    tri = []
    while n > 0:
        tri.append(n % 3)
        n //= 3
    for i, t in enumerate(tri):
        answer += t * (3 ** i)
    return answer