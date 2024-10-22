n = int(input())
cnt_list = []

for i in range((n // 3) + 1):
    if (n - 3*i) % 5 == 0:
        j = (n - 3*i) // 5
        cnt_list.append(i + j)

if len(cnt_list) == 0:
    print(-1)
else:
    print(min(cnt_list))