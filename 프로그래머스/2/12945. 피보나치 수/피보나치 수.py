def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    fibo = [0, 1] + [0 for _ in range(2, n + 1)]
    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    return fibo[n] % 1234567