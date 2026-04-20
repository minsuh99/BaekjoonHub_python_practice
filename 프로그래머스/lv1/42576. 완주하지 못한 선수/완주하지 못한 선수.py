from collections import defaultdict

def solution(participant, completion):
    answer = ''
    my_dict = defaultdict(int)
    
    for p in participant:
        if p not in my_dict:
            my_dict[p] = 1
        else:
            my_dict[p] += 1
    
    for c in completion:
        my_dict[c] -= 1
    
    for key in my_dict.keys():
        if my_dict[key] == 1:
            return key