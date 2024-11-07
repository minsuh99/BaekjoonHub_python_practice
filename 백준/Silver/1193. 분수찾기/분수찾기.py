def cal_sum(x):
    return int(x * (x + 1) / 2)

n = int(input())
cnt = 1

while True:
    if n <= cal_sum(cnt):
        break
    cnt += 1

if cnt % 2 == 0:
    print(f'{cnt - (cal_sum(cnt) - n)}/{(cal_sum(cnt) - n)+1}')
    
else:
    print(f'{(cal_sum(cnt) - n)+1}/{cnt - (cal_sum(cnt) - n)}')