def solution(s):
    answer = []
    temp = s[2:-2].split("},{")
    temp = [i.split(",") for i in temp]
    temp.sort(key=len)
    temp = [set(i) for i in temp]
    
    for i in range(len(temp)):
        value = list(temp[i] - set(answer))[0]
        answer.append(value)
    
    answer = [int(i) for i in answer]
    
    return answer