def count_k(n, k):
    res = 0
    temp = k
    
    while temp <= n:
        res += n // temp
        temp *= k
    
    return res

n, m = map(int, input().split())

count_2 = count_k(n, 2) - count_k(m, 2) - count_k(n-m , 2)
count_5 = count_k(n, 5) - count_k(m, 5) - count_k(n-m , 5)

print(min(count_2, count_5))
