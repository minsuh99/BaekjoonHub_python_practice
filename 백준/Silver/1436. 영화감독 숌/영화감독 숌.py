# disaster_num = []
# num = 666
# while len(disaster_num) <= 10000:
#     if str(num).find('666') != -1:
#         disaster_num.append(num)
#     num += 1
# print(disaster_num[int(input())-1])

# 1192 ms

disaster_num = []
num = 666
N = int(input())
while len(disaster_num) < N:
    if str(num).find('666') != -1:
        disaster_num.append(num)
    num += 1
print(disaster_num[-1])

# 1184ms
# while 때문인듯

N = int(input())
count = 0
num = 666

while True:
    if '666' in str(num):
        count += 1
    if count == N:
        print(num)
        break
    num += 1
    
# 584ms
# 리스트도 한 몫 하는듯
