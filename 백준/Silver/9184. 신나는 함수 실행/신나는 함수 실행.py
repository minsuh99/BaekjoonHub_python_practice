import sys
my_list = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                my_list[i][j][k] = 1
            elif i < j and j < k:
                my_list[i][j][k] = my_list[i][j][k-1] + my_list[i][j-1][k-1] - my_list[i][j-1][k]
            else:
                my_list[i][j][k] = my_list[i-1][j][k] + my_list[i-1][j-1][k] + my_list[i-1][j][k-1] - my_list[i-1][j-1][k-1]
            

input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    exit_condition = (a == -1) & (b == -1) & (c == -1)
    if exit_condition:
        break
    if a <= 0 or b <= 0 or c <= 0:
        ans = 1
    elif a > 20 or b > 20 or c > 20:
        ans = my_list[20][20][20]
    else:
        ans = my_list[a][b][c]
    print(f"w({a}, {b}, {c}) = {ans}")