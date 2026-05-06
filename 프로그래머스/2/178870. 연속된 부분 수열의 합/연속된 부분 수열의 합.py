def solution(sequence, k):
    n = len(sequence)
    start, end = 0, 0
    answer = [0, n - 1]
    cur_sum = sequence[0]
    
    while end < n:
        if cur_sum == k:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            cur_sum -= sequence[start]
            start += 1
        
        elif cur_sum > k:
            cur_sum -= sequence[start]
            start += 1
        
        else:
            end += 1
            if end < n:
                cur_sum += sequence[end]
    
    return answer