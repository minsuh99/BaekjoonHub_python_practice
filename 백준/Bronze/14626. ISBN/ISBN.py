isbn = input()
check_idx = 0
m = int(isbn[-1])
temp = 0

for i in range(len(isbn) - 1):
    if isbn[i] == "*":
        check_idx = i
    elif i % 2 == 0:
        temp += int(isbn[i])
    elif i % 2 != 0:
        temp += int(isbn[i]) * 3

flag = (check_idx % 2 == 0)
for num in range(10):
    if flag:
        if (temp + num) % 10 == (10 - m) % 10:
            print(num)
            exit()
    else:
        if (temp + num * 3) % 10 == (10 - m) % 10:
            print(num)
            exit()