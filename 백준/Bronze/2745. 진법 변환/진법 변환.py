input_list = input().split()
num = input_list[0][::-1]
b = int(input_list[1])
res = 0

for i in range(len(num)):
    if num[i].isdigit():
        res += int(num[i]) * (b ** i)
    elif num[i].isalpha():
        res += (ord(num[i]) - ord('A') + 10) * (b ** i)

print(res)
