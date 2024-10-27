num, b = map(int, input().split())
res = ''
power = 0
while True:
    if num < pow(b, power):
        break
    power += 1

while True:
    for i in range(power-1, -1, -1):
        for j in range(b-1, -1, -1):
            if num - j * pow(b, i) >= 0:
                break
        num -= j * pow(b, i)
        if j >= 10:
            res += chr(ord('A') + j - 10)
        else:
            res += str(j)
    if num <= 0:
        break

print(res)
