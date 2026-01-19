import sys
input = sys.stdin.readline

board = []
blank = []

for i in range(9):
    temp = list(map(int, input().split()))
    for j in range(9):
        if temp[j] == 0:
            blank.append((i, j))
    board.append(temp)


def check(num, blank_r, blank_c):
    for c in range(9):
        if c == blank_c:
            continue
        if board[blank_r][c] == num:
            return False
        
    for r in range(9):
        if r == blank_r:
            continue
        if board[r][blank_c] == num:
            return False
    
    for r in range((blank_r // 3) * 3, (blank_r // 3 + 1) * 3):
        for c in range((blank_c // 3) * 3, (blank_c // 3 + 1) * 3):
            if r == blank_r and c == blank_c:
                continue
            if board[r][c] == num:
                return False
    
    return True


def backtracking(idx):
    if idx == len(blank):
        for i in range(9):
            print(*board[i])
        exit()
    
    br, bc = blank[idx]
    for n in range(1, 10):
        if check(n, br, bc):
            board[br][bc] = n
            backtracking(idx + 1)
            board[br][bc] = 0

backtracking(0)