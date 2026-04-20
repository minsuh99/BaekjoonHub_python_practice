def solution(s):
    answer = 0
    first_alpha = ''
    cnt1 = 0
    cnt2 = 0
    for alpha in s:
        if first_alpha == "":
            first_alpha = alpha
            cnt1 += 1
        else:
            if first_alpha != alpha:
                cnt2 += 1
                if cnt1 == cnt2:
                    answer += 1
                    cnt1, cnt2 = 0, 0
                    first_alpha = ""
            else:
                cnt1 += 1
    if first_alpha != "":
        answer += 1
    return answer