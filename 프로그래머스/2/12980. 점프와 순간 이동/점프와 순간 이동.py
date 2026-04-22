def solution(n):
    res = 0
    
    while n > 0:
        if n % 2 != 0:
            n -= 1
            res += 1
        else:
            n //= 2
    
    return res