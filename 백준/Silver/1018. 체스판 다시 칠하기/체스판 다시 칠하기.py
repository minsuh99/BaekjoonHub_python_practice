import sys
input = sys.stdin.readline

N, M = map(int, input().split())

my_list = []
res = 64

for _ in range(N):
    my_list.append(list(input().rstrip()))

for row in range(N - 7):
    for col in range(M - 7):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    if my_list[row + i][col + j] != "W":
                        cnt += 1
                else:
                    if my_list[row + i][col + j] != "B":
                        cnt += 1
        
        res = min(res, cnt, 64 - cnt)

print(res)