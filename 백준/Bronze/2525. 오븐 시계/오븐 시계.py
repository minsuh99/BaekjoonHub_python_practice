def alarm(h, m, c):
    m += c
    if m >= 60:
        h += (m // 60)
        m %= 60
        if h >= 24:
            h %= 24
    print(h, m)
    
h, m = map(int, input().split())
c = int(input())
alarm(h, m, c)