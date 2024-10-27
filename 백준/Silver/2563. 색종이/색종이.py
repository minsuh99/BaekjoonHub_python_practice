my_mat = [[0 for _ in range(101)] for _ in range(101)]
res = 0
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            my_mat[i][j] = 1

for i in range(100):
    res += sum(my_mat[i])

print(res)