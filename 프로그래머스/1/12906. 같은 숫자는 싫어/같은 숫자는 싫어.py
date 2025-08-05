def solution(arr):
    answer = []
    for i, num in enumerate(arr):
        if not answer or num != answer[-1]:
            answer.append(num)
            
    return answer