def solution(food):
    answer = ''
    temp = ''
    for i, num in enumerate(food):
        if i == 0:
            continue
        temp += str(i) * (num // 2)
    answer = temp + '0' + temp[::-1]
    return answer