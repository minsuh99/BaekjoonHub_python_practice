def solution(s):
    answer = ''
    flag = False
    
    for alpha in s:
        if alpha != " ":
            if not flag:
                answer += alpha.upper()
                flag = True
            else:
                answer += alpha.lower()
                
        else:
            answer += alpha
            flag = False
    return answer