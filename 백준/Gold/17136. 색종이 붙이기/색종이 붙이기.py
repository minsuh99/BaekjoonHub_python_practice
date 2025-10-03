import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M = []
for _ in range(10):
    M.append(list(map(int, input().split())))

paper = [0, 5, 5, 5, 5, 5]
res = 26

def backtrack(pos, used):
    global res
    if used >= res:
        return
    
    while pos < 100 and M[pos // 10][pos % 10] == 0:
        pos += 1
    
    if pos == 100:
        res = min(res, used)
        return
    
    row = pos // 10
    col = pos % 10  
    
    if M[row][col] == 1:
        for size in range(5, 0, -1):
            flag = True
            if paper[size] > 0:
                if row + size <= 10 and col + size <= 10:
                    for i in range(row, row+size):
                        for j in range(col, col+size):
                            if M[i][j] != 1:
                                flag = False
                        if flag == False:
                            break
                else:
                    flag = False
            else:
                flag = False
            if flag == True:
                paper[size] -= 1
                for i in range(row, row+size):
                    for j in range(col, col+size):
                        M[i][j] = 0
                        
                backtrack(pos + 1, used + 1)
                
                for i in range(row, row+size):
                    for j in range(col, col+size):
                        M[i][j] = 1
                
                paper[size] += 1
    else:
        backtrack(pos + 1, used)

backtrack(0, 0)
print(res if res != 26 else -1)