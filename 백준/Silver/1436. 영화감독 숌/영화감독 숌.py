disaster_num = []
num = 666
N = int(input())
while len(disaster_num) < N:
    if str(num).find('666') != -1:
        disaster_num.append(num)
    num += 1
print(disaster_num[-1])