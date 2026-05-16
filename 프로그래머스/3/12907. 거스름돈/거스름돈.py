def solution(n, money):
    answer = 0
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
    answer = dp[n]
    return answer