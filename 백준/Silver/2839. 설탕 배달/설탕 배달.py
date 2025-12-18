N = int(input())

cnt_3 = 0
cnt_5 = 0

while True:
    if N % 5 == 0:
        cnt_5 = N // 5
        break
    
    if N < 3:
        print(-1)
        exit()
    
    N -= 3
    cnt_3 += 1
    
print(cnt_3 + cnt_5)