N = int(input())
my_list = []
rank = [1] * N
for _ in range(N):
    x, y = map(int, input().split())
    my_list.append((x,y))

for i in range(len(my_list)):
    for j in range(len(my_list)):
        if i==j: continue
        elif (my_list[i][0] < my_list[j][0]) & (my_list[i][1] < my_list[j][1]):
            rank[i] += 1

for i in range(len(rank)):
    print(rank[i], end=" ")