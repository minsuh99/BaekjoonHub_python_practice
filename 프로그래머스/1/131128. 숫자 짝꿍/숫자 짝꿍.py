from collections import Counter


def solution(X, Y):
    answer = ''
    dict_x, dict_y = Counter(X), Counter(Y)
    my_dict = {}
    
    for k in dict_x:
        if k in dict_y:
            my_dict[k] = min(dict_x[k], dict_y[k])
    
    if not my_dict:
        return "-1"
    
    if list(my_dict.keys()) == ['0']:
        return "0"
    
    my_dict = dict(sorted(my_dict.items(), reverse=True))

    for k in my_dict:
        answer += str(k) * my_dict[k]
    
    return answer