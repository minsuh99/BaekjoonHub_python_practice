import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []

for _ in range(R):
    board.append(list(input().rstrip()))

drdc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0
res_set = set()
res_set.add(board[0][0])

def dfs(cur_r, cur_c, cnt):
    global res
    res = max(res, cnt)
    
    if res >= 26:
        print(res)
        exit()
    
    for dr, dc in drdc:
        nr = cur_r + dr
        nc = cur_c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] not in res_set:
                res_set.add(board[nr][nc])
                dfs(nr, nc, cnt + 1)
                res_set.remove(board[nr][nc])


dfs(0, 0, 1)
print(res)