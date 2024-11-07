def alarm(h, m):
    if m - 45 < 0:
        m += 60
        if h == 0:
            h = 24
        h -= 1
    m -= 45
    print(h, m)
    
h, m = map(int, input().split())
alarm(h, m)