def solution(clothes):
    answer = 1
    my_dict = dict()
    for cloth in clothes:
        if cloth[1] not in my_dict:
            my_dict[cloth[1]] = 1
        else:
            my_dict[cloth[1]] += 1
    
    print(my_dict)
    
    for key in my_dict:
        answer *= (my_dict[key] + 1)
    return answer - 1