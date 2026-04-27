def solution(begin, target, words):
    answer = len(words) + 1
    if target not in words:
        return 0
    visited = [False for _ in range(len(words))]
    
    def dfs(start, cur_word, cur_list):
        nonlocal answer, visited
        
        if cur_word == target:
            answer = min(answer, len(cur_list))
            return
        
        for i in range(start, len(words)):
            cnt = 0
            for cur_word_alpha, words_alpha in zip(cur_word, words[i]):
                if cur_word_alpha != words_alpha:
                    cnt += 1
            
            if not visited[i] and cnt == 1:
                visited[i] = True
                cur_list.append(words[i])
                dfs(start, words[i], cur_list)
                cur_list.pop()
                visited[i] = False
            
    dfs(0, begin, [])
    
    return answer