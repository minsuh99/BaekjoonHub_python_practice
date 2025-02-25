def solution(n):
    answer = 0
    chess_board = [[0 for _ in range(n)] for _ in range(n)]
    
    def put_queens(row, col):
        for i in range(row): # 같은 열인지 체크
            if chess_board[i][col]:
                return False
        
        for i in range(1, row + 1): # 대각선 체크
            condition1 = ((row - i >= 0) and (col - i >= 0) and (chess_board[row - i][col - i] == 1)) # 왼쪽 위 대각선 체크
            condition2 = ((row - i >= 0) and (col + i < n) and (chess_board[row - i][col + i] == 1)) # 오른쪽 위 대각선 체크
            # condition3 = ((row + i < n) and (col - i >= 0) and (chess_board[row + i][col - i] == 0)) # 왼쪽 아래 대각선 체크
            # condition4 = ((row + i < n) and (col + i < n) and (chess_board[row + i][col + i] == 0)) # 오른쪽 아래 대각선 체크
            
            # if not (condition1 and condition2 and condition3 and condition4):
            #     return False
            if condition1:
                return False
            if condition2:
                return False
        return True
        
    
    def backtrack(row):
        nonlocal answer
        if row == n:
            answer += 1
            return
        
        for col in range(n):
            if put_queens(row, col):
                chess_board[row][col] = 1
                backtrack(row + 1)
                chess_board[row][col] = 0
    backtrack(0)
        
    return answer