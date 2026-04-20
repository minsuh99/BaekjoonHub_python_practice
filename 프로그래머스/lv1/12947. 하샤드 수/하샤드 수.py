def solution(x):
    hashad_check = sum([int(i) for i in str(x)])
    answer = True if x % hashad_check == 0 else False
    return answer