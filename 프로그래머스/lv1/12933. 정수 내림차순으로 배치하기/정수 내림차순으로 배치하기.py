def solution(n):
    answer = int("".join(sorted([i for i in str(n)], reverse=True)))
    return answer