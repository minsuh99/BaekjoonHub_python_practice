def solution(dartResult):
    answer = [0, 0, 0]
    results = []
    temp = ''
    
    for result in dartResult:
        if result.isdigit():
            if temp != "":
                if not temp[-1].isdigit():
                    results.append(temp)
                    temp = ""
            temp += result
        elif result.isalpha():
            temp += result
        elif result in ["*", "#"]:
            temp += result
            results.append(temp)
            temp = ""
    if temp:
        results.append(temp)
    
    for i, res in enumerate(results):
        if res[-1] in ["*", "#"]:
            if res[-2] == "S":
                answer[i] += int(res[:-2])
            elif res[-2] == "D":
                answer[i] += int(res[:-2]) ** 2
            elif res[-2] == "T":
                answer[i] += int(res[:-2]) ** 3
                
            if res[-1] == "*":
                if i == 0:
                    answer[i] *= 2
                else:
                    answer[i] *= 2
                    answer[i - 1] *= 2
            elif res[-1] == "#":
                answer[i] *= -1
                
        else:
            if res[-1] == "S":
                answer[i] += int(res[:-1])
            elif res[-1] == "D":
                answer[i] += int(res[:-1]) ** 2
            elif res[-1] == "T":
                answer[i] += int(res[:-1]) ** 3
    return sum(answer)