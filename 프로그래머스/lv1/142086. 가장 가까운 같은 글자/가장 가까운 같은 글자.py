def solution(s):
    answer = []
    alpha_idx = [-1 for _ in range(26)]
    
    for i, alpha in enumerate(s):
        idx = ord(alpha) - ord('a')
        if alpha_idx[idx] == -1:
            answer.append(-1)
        else:
            answer.append(i - alpha_idx[idx])
        alpha_idx[idx] = i
    return answer