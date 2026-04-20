def solution(s, skip, index):
    answer = ''
    use_alpha = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in skip]
    
    for alpha in s:
        idx = use_alpha.index(alpha)
        answer += use_alpha[(idx + index) % len(use_alpha)]
            
    return answer