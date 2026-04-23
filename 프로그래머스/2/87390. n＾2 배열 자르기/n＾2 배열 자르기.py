def solution(n, left, right):
    answer = []
    for idx in range(left, right + 1):
        temp = max(idx // n, idx % n) + 1
        answer.append(temp)
    
    return answer