def solution(n):
    answer = 0
    start, end = 1, 1
    while end <= n:
        partial_sum = sum(range(start, end + 1))
        if partial_sum <= n:
            if partial_sum == n:
                answer += 1
            end += 1
        else:
            start += 1
    return answer