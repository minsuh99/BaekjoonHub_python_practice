from collections import deque


def solution(board, moves):
    answer = 0
    new_board = [deque([k for k in list(i) if k > 0]) for i in (list(zip(*board)))]
    stack = []
    
    for move in moves:
        if new_board[move - 1]:
            cur_doll = new_board[move - 1].popleft()
            if stack and stack[-1] == cur_doll:
                stack.pop()
                answer += 2
            else:
                stack.append(cur_doll)
    return answer