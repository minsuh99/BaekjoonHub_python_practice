T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    people = list(range(1, n+1))
    for _ in range(k):
        temp = [0] * n
        for i in range(n):
            temp[i] = sum(people[:i+1])
        people = temp
    print(temp[n-1])