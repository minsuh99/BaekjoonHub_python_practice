def solution(board, moves):
    answer = 0
    cur_board = []
    basket = []
    for lst in (zip(*board)):
        cur_board.append([i for i in lst if i > 0])
    for move in moves:
        if not cur_board[move - 1]:
            continue
        else:
            doll = cur_board[move - 1].pop(0)
        if not basket or basket[-1] != doll:
            basket.append(doll)
        else:
            answer += 2
            basket.pop()
    return answer