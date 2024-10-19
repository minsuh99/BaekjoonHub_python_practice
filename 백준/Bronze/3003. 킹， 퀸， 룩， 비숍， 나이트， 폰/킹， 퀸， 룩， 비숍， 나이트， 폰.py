chess = [1, 1, 2, 2, 2, 8]

my_list = [int(i) for i in input().split()]

for i in range(len(chess)):
    print(chess[i]-my_list[i], end=" ")