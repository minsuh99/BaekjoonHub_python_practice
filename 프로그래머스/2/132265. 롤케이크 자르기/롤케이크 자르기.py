from collections import Counter


def solution(topping):
    answer = 0
    left_set = set()
    my_dict = Counter(topping)

    for t in topping:
        left_set.add(t)
        my_dict[t] -= 1
        if my_dict[t] == 0:
            del my_dict[t]
        
        if len(left_set) == len(my_dict):
            answer += 1
            
    
    
    return answer