from itertools import combinations


def solution(numbers):
    answer = []
    
    for comb in list(combinations(numbers, 2)):
        answer.append(sum(comb))
    
    answer = sorted(list(set(answer)))
    
    return answer