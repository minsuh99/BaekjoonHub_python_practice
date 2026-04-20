def solution(s, n):
    answer = ''
    for alpha in s:
        if alpha == " ":
            answer += alpha
        else:
            if alpha.isupper():
                temp = ord(alpha) + n
                if temp > ord('Z'):
                    temp -= 26
            elif alpha.islower():
                temp = ord(alpha) + n
                if temp > ord('z'):
                    temp -= 26
            answer += chr(temp)
        
    return answer