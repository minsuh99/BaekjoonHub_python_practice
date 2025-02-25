def solution(k, dungeons):
    answer = -1
    visited = [False for _ in range(len(dungeons))]
    
    def backtrack(cur_k, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            if not visited[i]:
                min_k, minus_k = dungeons[i]
                if cur_k >= min_k:
                    visited[i] = True
                    backtrack(cur_k - minus_k, count + 1)
                    visited[i] = False
    backtrack(k, 0)
    return answer