def solution(name, yearning, photo):
    answer = []
    my_dict = {}
    for k, v in zip(name, yearning):
        my_dict[k] = v
    
    for p in photo:
        score = 0
        for n in p:
            if n in my_dict:
                score += my_dict[n]
        answer.append(score)
    return answer