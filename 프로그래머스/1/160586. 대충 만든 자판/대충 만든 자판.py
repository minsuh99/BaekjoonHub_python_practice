def solution(keymap, targets):
    answer = []
    my_dict = {}
    for k in keymap:
        for i, alpha in enumerate(k):
            if alpha not in my_dict:
                my_dict[alpha] = i + 1
            else:
                my_dict[alpha] = min(my_dict[alpha], i + 1)
    
    for target in targets:
        cnt = 0
        flag = False
        for alpha in target:
            if alpha in my_dict:
                cnt += my_dict[alpha]
            else:
                answer.append(-1)
                flag = True
                break
        if flag:
            continue
        answer.append(cnt)
    return answer