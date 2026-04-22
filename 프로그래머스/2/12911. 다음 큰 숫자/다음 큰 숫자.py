def solution(n):
    cnt_1 = bin(n).count("1")
    
    while True:
        n += 1
        if cnt_1 == bin(n).count("1"):
            break
            
    return n