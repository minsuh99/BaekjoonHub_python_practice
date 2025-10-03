import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
res = 0
cols = [False for _ in range(N)]
sum_diag = [False for _ in range(2*N + 1)]
diff_diag = [False for _ in range(2*N + 1)]

def backtrack(row):
    global res
    if row == N:
        res += 1
        return
    
    for col in range(N):
        if cols[col] == False and sum_diag[row+col] == False and diff_diag[row-col+N-1] == False:
            cols[col] = sum_diag[row+col] = diff_diag[row-col+N-1] = True
            backtrack(row + 1)
            cols[col] = sum_diag[row+col] = diff_diag[row-col+N-1] = False
            

backtrack(0)
print(res)