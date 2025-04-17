from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    my_list = sorted(dict(Counter(tangerine)).items(), key=lambda x:-x[1])
    # [1, 3, 2, 5, 4, 5, 2, 3] -> [(3, 2), (2, 2), (5, 2), (1, 1), (4, 1)]
    
    temp = 0    
    for num in my_list:
        temp += num[1]
        answer += 1
        if temp >= k:
            break
    return answer