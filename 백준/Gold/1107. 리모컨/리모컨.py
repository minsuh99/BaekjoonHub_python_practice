N = int(input())
M = int(input())
broken_list = []
res = 0

if M > 0:
    broken_list = [int(i) for i in input().split()]

normal_list = [int(i) for i in range(10) if i not in broken_list]

# + / - 로만 이동하는 경우 먼저 저장
res = abs(N - 100)
if res == 0:
    print(res)
    exit()

# 숫자키로 채널 이동 후, + / - 로 조작
# 0 ~ 999999 전부다 체크

for channel in range(1000000):
    flag = False
    cur_cnt = 0
    # 만들 수 있는 채널인지를 검사
    for num in str(channel):
        if int(num) in broken_list:
            flag = True
            break
    if flag:
        continue
    
    cur_cnt = len(str(channel)) + abs(N - channel)
    res = min(res, cur_cnt)

print(res)