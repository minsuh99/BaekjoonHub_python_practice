import sys
input = sys.stdin.readline

def max_counting(my_list):
    res = 0
    row = len(my_list)
    col = len(my_list[0])
    
    for r in range(row):
        row_cnt = 1
        for c in range(col - 1):
            if my_list[r][c] == my_list[r][c + 1]:
                row_cnt += 1
                res = max(res, row_cnt)
            else:
                row_cnt = 1
    
    for c in range(col):
        col_cnt = 1
        for r in range(row - 1):
            if my_list[r][c] == my_list[r + 1][c]:
                col_cnt += 1
                res = max(res, col_cnt)
            else:
                col_cnt = 1

    return res

N = int(input())
candy = []
res = 0

for _ in range(N):
    candy.append(list(input().rstrip()))

row = len(candy)
col = len(candy[0])

res = max_counting(candy)
if res == N:
    print(N)
    exit()

for r in range(row):
    for c in range(col - 1):
        candy[r][c], candy[r][c + 1] = candy[r][c + 1], candy[r][c]
        res = max(res, max_counting(candy))
        if res == N:
            print(N)
            exit()
        candy[r][c], candy[r][c + 1] = candy[r][c + 1], candy[r][c]

for c in range(col):
    for r in range(row - 1):
        candy[r][c], candy[r + 1][c] = candy[r + 1][c], candy[r][c]
        res = max(res, max_counting(candy))
        if res == N:
            print(N)
            exit()
        candy[r][c], candy[r + 1][c] = candy[r + 1][c], candy[r][c]

print(res)