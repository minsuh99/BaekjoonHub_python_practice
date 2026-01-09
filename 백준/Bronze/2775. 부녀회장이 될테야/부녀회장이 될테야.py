import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    
    res = [i for i in range(1, n + 1)]
    
    for _ in range(k):
        temp = 0
        for j in range(n):
            temp += res[j]
            res[j] = temp
        
    
    print(res[-1])