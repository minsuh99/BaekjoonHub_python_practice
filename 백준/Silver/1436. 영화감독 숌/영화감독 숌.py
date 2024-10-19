disaster_num = []
num = 666
while len(disaster_num) <= 10000:
    if str(num).find('666') != -1:
        disaster_num.append(num)
    num += 1
print(disaster_num[int(input())-1])