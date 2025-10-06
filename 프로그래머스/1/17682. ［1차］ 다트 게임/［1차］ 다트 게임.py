def solution(dartResult):
    answer = 0
    chance = 0
    score = [0 for _ in range(4)]
    temp = ''
    for dart in dartResult:
        if dart.isdigit():
            temp += dart
        else:
            if dart == "S":
                chance += 1
                score[chance] = int(temp)
                score[chance] = score[chance] ** 1
                temp = ''
            elif dart == "D":
                chance += 1
                score[chance] = int(temp)
                score[chance] = score[chance] ** 2
                temp = ''
            elif dart == "T":
                chance += 1
                score[chance] = int(temp)
                score[chance] = score[chance] ** 3
                temp = ''
            elif dart == "*":
                if chance == 1:
                    score[chance] *= 2
                else:
                    score[chance - 1] *= 2
                    score[chance] *= 2
            elif dart == "#":
                    score[chance] *= -1
    
    answer = sum(score)
    print(score)
    
    return answer