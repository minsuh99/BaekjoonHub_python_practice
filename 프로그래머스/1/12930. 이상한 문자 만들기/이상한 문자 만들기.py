def solution(s):
    answer = ''
    idx = 0
    for alpha in s:
        if alpha == " ":
            answer += alpha
            idx = 0
        else:
            if idx % 2 == 0:
                answer += alpha.upper()
            else:
                answer += alpha.lower()
            idx += 1
    return answer