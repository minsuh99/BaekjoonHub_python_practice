def solution(land):
    answer = 0
    dp = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    dp[0] = land[0].copy()
    
    for r in range(1, len(dp)):
        for c in range(len(dp[0])):
            dp[r][c] = max([value for i, value in enumerate(dp[r - 1]) if i != c]) + land[r][c]
        
    return max(dp[-1])