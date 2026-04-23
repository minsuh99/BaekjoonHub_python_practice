from collections import Counter


def solution(want, number, discount):
    answer = 0
    if len(set(want) & set(discount)) == 0:
        return answer
    
    want_dict = {k:v for k, v in zip(want, number)}
    
    for i in range(len(discount) - 9):
        if want_dict == dict(Counter(discount[i:i+10])):
            answer += 1
    
    return answer