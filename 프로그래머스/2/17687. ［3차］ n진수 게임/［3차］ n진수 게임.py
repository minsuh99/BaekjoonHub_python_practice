def solution(n, t, m, p):
    res = ""
    answer = '0'
    num = 0
    while len(answer) < t * m:
        x = num
        temp = ""

        if x == 0:
            temp = "0"
        else:
            while x > 0:
                digit = x % n
                if digit >= 10:
                    temp = chr(ord("A") + digit - 10) + temp
                else:
                    temp = str(digit) + temp
                x //= n

        answer += temp
        num += 1
    
    for s in range(p, t * m + 1, m):
        res += answer[s]
    return res