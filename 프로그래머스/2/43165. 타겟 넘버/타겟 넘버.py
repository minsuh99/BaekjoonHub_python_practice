import sys
sys.setrecursionlimit(10 ** 9)


def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(cur_idx, cur_sum):
        nonlocal answer, numbers, target
        nonlocal n
        
        if cur_idx == n:
            if cur_sum == target:
                answer += 1
            return
        
        dfs(cur_idx + 1, cur_sum - numbers[cur_idx])
        dfs(cur_idx + 1, cur_sum + numbers[cur_idx])
        
        
    dfs(0, 0)
                
    
    return answer