N = int(input())
check_num = 666
cnt = 0

while True:
    if '666' in str(check_num):
        cnt += 1
    if cnt == N:
        print(check_num)
        exit()
    check_num += 1