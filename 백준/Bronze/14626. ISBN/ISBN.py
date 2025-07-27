isbn = input()
answer = 0
target_idx = 0

for i in range(len(isbn)-1):
    if isbn[i] == "*":
        target_idx = i
        pass
    elif i % 2 != 0:
        answer += (3 * int(isbn[i]))
    else:
        answer += int(isbn[i])

target = int(isbn[-1])

for i in range(10):
    temp = i if target_idx % 2 == 0 else 3 * i
    if (10 - (answer + temp) % 10) % 10 == target:
        print(i)
        break