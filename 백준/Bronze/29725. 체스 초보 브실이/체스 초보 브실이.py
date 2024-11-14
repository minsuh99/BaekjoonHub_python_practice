def check_score(s: str):
    score = 0
    if s == 'k':
        score = 0
    elif s == 'p':
        score = 1
    elif s == 'n' or s == 'b':
        score = 3
    elif s == 'r':
        score = 5
    elif s == 'q':
        score = 9

    return score


check_board = [''] * 8
for i in range(len(check_board)):
    check_board[i] = input()
    
white_score = 0
black_score = 0


for i in range(len(check_board)):
    for j in range(len(check_board[i])):
        if check_board[i][j].isupper():
            white_score += check_score(check_board[i][j].lower())
        elif check_board[i][j].islower():
            black_score += check_score(check_board[i][j])
        elif check_board[i][j] == '.':
            pass

print(white_score - black_score)