def solution(n):
    # n = 1 -> answer = 1 [(1)]
    # n = 2 -> answer = 2 [(1, 1), (2)]
    # n = 3 -> answer = 3 [(1, 1, 1), (2, 1), (1, 2)]
    # n = 4 -> answer = 5 [(1, 1, 1, 1), (1, 2, 1), (2, 1, 1), (1, 1, 2), (2, 2)]
    # n = 5 -> answer = 8 [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 1, 1), (2, 1, 1, 1), (1, 2, 2), (2, 1, 2), (2, 2, 1)]
    # Fibonacci
    
    num_list = [1 for _ in range(60001)]
    for i in range(2, n+1):
        # num_list[i] = num_list[i-2] + num_list[i-1]
        num_list[i] = (num_list[i-2] + num_list[i-1]) % 1000000007
    # answer = (num_list[n] % 1000000007)
    answer = num_list[n]
    
    
    return answer