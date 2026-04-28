def solution(n, k):
    answer = 0
    base_k = "" if k != 10 else str(n)
    while n > 0 and k != 10:
        base_k = str(n % k) + base_k
        n //= k
    temp = [int(num) for num in base_k.split("0") if num]
    
    for num in temp:
        flag = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = False
                break
        if flag and num > 1:
            answer += 1
            
    return answer