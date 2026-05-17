def solution(m, n, board):
    answer = 0
    board = [[board[row][col] for row in range(m)] for col in range(n)]
    # 높이 m, 폭 n -> 높이 n, 폭 m으로 바꿈
    
    while True:
        change_rc = set() # 중복 있을수도 있으니 set으로
        for r in range(n - 1):
            for c in range(m - 1):
                if board[r][c] != "":   # 빈칸이 아니라면
                    # 2*2 형태로 같은게 4개 있다면
                    if board[r][c] == board[r + 1][c] == board[r][c + 1] == board[r + 1][c + 1]: 
                        # 빈칸으로 변해야 할 좌표들 추가
                        change_rc.add((r, c))
                        change_rc.add((r + 1, c))
                        change_rc.add((r, c + 1))
                        change_rc.add((r + 1, c + 1))

        
        if not change_rc: # 빈칸으로 변해야 할게 없다면
            return answer # 정답 반환
        else:
            answer += len(change_rc)
            
            for r, c in change_rc: # 빈칸 변환
                board[r][c] = ""
            
            # 위에 있는 블록들 아래로 내려보내기
            for r in range(n):
                temp = []
                cnt = 0
                for c in range(m):
                    if board[r][c] != "":
                        temp.append(board[r][c])
                    else:
                        cnt += 1
                
                board[r] = ["" for _ in range(cnt)] + temp

    return answer