from collections import Counter

def solution(topping):
    answer = 0
    
    cur_topping = dict(Counter(topping))
    
    young_brother = set(topping)
    old_brother = set()
    
    for t in topping:
        old_brother.add(t)
        cur_topping[t] -= 1
        if cur_topping[t] == 0:
            young_brother.remove(t)
            # young_brother -= set([t])
        
        if len(old_brother) == len(young_brother):
            answer += 1        
    
    return answer