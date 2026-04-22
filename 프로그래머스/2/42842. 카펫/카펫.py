def solution(brown, yellow):
    answer = []
    area = brown + yellow
    
    for i in range(2, int(area ** 0.5) + 1):
        if area % i == 0:
            if (area // i - 2) * (i - 2) == yellow:
                answer = [area // i, i]
                break
    return answer