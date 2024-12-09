num_list = [1, 1]
for i in range(2, 41):
    num_list.append(num_list[i-2] + num_list[i-1])

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(num_list[n])