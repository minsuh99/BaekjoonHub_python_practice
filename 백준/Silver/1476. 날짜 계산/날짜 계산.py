E, S, M = map(int, input().split())

max_E = 15
max_S = 28
max_M = 19

while True:
    if E == S and S == M:
        print(E)
        exit()
    
    min_year = min(E, S, M)
    if E == min_year:
        E += max_E
    elif S == min_year:
        S += max_S
    elif M == min_year:
        M += max_M

