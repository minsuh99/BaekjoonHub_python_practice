def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]

    while True:
        bomb = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0:
                    if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                        bomb.add((i, j))
                        bomb.add((i, j+1))
                        bomb.add((i+1, j))
                        bomb.add((i+1, j+1))

        if len(bomb) == 0:
            break

        for i, j in bomb:
            board[i][j] = 0

        answer += len(bomb)
        ## 다운,,

        temp_board = list(zip(*board))
        for i in range(len(temp_board)):
            new_line = [i for i in temp_board[i] if i != 0]
            new_line = [0 for _ in range(len(temp_board[i]) - len(new_line))] + new_line
            temp_board[i] = new_line

        temp_board2 = list(zip(*temp_board))
        board = [list(i) for i in temp_board2]

    return answer