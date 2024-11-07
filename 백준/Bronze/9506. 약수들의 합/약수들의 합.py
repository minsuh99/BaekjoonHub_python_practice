while True:
    n = int(input())
    if n == -1:
        break
    fac_list = []
    
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            fac_list.append(i)
            fac_list.append(n // i)
    fac_list = sorted(fac_list)[:-1]
    if n == sum(fac_list):
        fac_list = [str(i) for i in fac_list]
        print(f'{n} = {" + ".join(fac_list)}')
    else:
        print(f'{n} is NOT perfect.')