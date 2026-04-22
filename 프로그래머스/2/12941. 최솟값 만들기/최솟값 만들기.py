def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for n, m in zip(A, B):
        answer += n * m
    

    return answer