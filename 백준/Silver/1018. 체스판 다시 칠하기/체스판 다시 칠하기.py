n, m = map(int,input().split())
chess_board = []
res = []
check_list1 = ['B', 'W']
check_list2 = ['W', 'B']

for _ in range(n):
    chess_board.append(list(input()))

for i in range(n-7): # row
    for j in range(m-7): #column
        cnt1 = 0
        cnt2 = 0
        new_chess = [row[j:j+8] for row in chess_board[i:i+8]]

        for r in range(8):
            for c in range(8):
                if new_chess[r][c] != check_list1[(r+c) % 2]:
                    cnt1 += 1
                if new_chess[r][c] != check_list2[(r+c) % 2]:
                    cnt2 += 1
                
                    
        res.append(min(cnt1, cnt2))

print(min(res))