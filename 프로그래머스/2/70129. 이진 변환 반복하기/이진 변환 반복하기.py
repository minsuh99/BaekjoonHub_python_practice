def solution(s):
    answer = []
    cnt_zero = 0
    cnt = 0
    
    while s != "1":
        cnt += 1
        new_s = s.replace("0", "")
        cnt_zero += len(s) - len(new_s)
        s = bin(len(new_s))[2:]
        
    answer = [cnt, cnt_zero]
    
    return answer

