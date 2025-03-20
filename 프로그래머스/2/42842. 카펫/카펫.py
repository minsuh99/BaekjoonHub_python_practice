def solution(brown, yellow):
    answer = []
    
    target = brown + yellow
    divisor = []
    
    for i in range(1, int(target ** (0.5))+1):
        if target % i == 0:
            divisor.append((target // i, i))
    
    for tup in divisor[::-1]:
        if (tup[0] - 2) * (tup[1] - 2) == yellow:
            return [tup[0], tup[1]]
    
    return answer