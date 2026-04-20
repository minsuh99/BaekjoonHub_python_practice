def solution(babbling):
    answer = 0
    
    for word in babbling:
        idx = 0
        prev = ""
        
        while True:
            cur = ""
            
            if word[idx:idx+3] in ["aya", "woo"]:
                cur = word[idx:idx+3]
            elif word[idx:idx+2] in ["ye", "ma"]:
                cur = word[idx:idx+2]
            else:
                break
            
            if cur == prev:
                break
            
            idx += len(cur)
            prev = cur
            
            if idx == len(word):
                answer += 1
                break
    
    return answer