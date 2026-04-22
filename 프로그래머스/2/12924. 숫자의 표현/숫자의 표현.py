def solution(n):
    answer = 0
    start, end = 1, 1
    partial_sum = 1
    while end <= n:
        if partial_sum <= n:
            if partial_sum == n:
                answer += 1
            end += 1
            partial_sum += end
        else:
            partial_sum -= start
            start += 1
            
    return answer