import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

tetromino_drdc = [
    # ㅡ자 도형
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # ㅁ자 도형
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # ㅣ_ 도형
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    # s자 도형
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (0, 1), (1, -1)],
    [(0, 0), (1, 0), (0, 1), (-1, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    # ㅗ 도형
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (1, -1), (2, 0)],
    [(0, 0), (0, 1), (-1, 1), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)]
]

res = 0

for row in range(N):
    for col in range(M):
        for drdc in tetromino_drdc:
            cur_score = 0
            flag = False
            for dr, dc in drdc:
                if 0 <= row + dr < N and 0 <= col + dc < M:
                    cur_score += board[row + dr][col + dc]
                else:
                    flag = True
                    break
            if not flag:
                res = max(res, cur_score)

print(res)