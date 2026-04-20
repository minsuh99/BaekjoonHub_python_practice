def solution(n):
    answer = 0
    num_of_div = [0 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            num_of_div[j] += 1
    
    answer = len([k for k in num_of_div if k == 2])
    return answer