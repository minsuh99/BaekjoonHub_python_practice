import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
visited = [[False for _ in range(M)] for _ in range(N)]
drdc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(N):
    board.append(list(input().rstrip()))


def dfs(r, c, pr, pc, depth):
    visited[r][c] = True

    for dr, dc in drdc:
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < N and 0 <= nc < M):
            continue

        if board[nr][nc] != board[r][c]:
            continue

        if visited[nr][nc] == False:
            if dfs(nr, nc, r, c, depth + 1):
                return True

        else:
            if (nr, nc) != (pr, pc) and depth >= 4:
                return True

    return False

for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            if dfs(r, c, -1, -1, 1):
                print("Yes")
                exit()

print("No")