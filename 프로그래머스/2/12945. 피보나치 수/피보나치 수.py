def solution(n):
    fibo_num = [0 for _ in range(100001)]
    fibo_num[1] = 1
    for i in range(2, n+1):
        fibo_num[i] = fibo_num[i-2] + fibo_num[i-1]
    
    answer = (fibo_num[n] % 1234567)
    
    return answer