while True:
    N = int(input())
    divisors = []
    if N == -1:
        exit()
    
    for i in range(1, N):
        if N % i == 0:
            divisors.append(i)
    
    if sum(divisors) == N:
        res = str(N) + " = " + " + ".join([str(i) for i in divisors])
        
        print(res)
    else:
        print(f"{N} is NOT perfect.")