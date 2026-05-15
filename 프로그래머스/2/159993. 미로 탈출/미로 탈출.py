from collections import deque


def solution(maps):
    answer = -1
    sr, sc = 0, 0

    drdc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    R, C = len(maps), len(maps[0])

    for r in range(R):
        for c in range(C):
            if maps[r][c] == "S":
                sr, sc = r, c
                break

    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[sr][sc] = True

    queue = deque([(sr, sc, 0)])

    while queue:
        cur_r, cur_c, cnt = queue.popleft()

        if maps[cur_r][cur_c] == "L":
            answer = cnt
            break

        for dr, dc in drdc:
            nr, nc = cur_r + dr, cur_c + dc

            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and maps[nr][nc] != "X":
                    visited[nr][nc] = True
                    queue.append((nr, nc, cnt + 1))

    if answer == -1:
        return -1

    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[cur_r][cur_c] = True

    queue = deque([(cur_r, cur_c, 0)])

    while queue:
        cur_r, cur_c, cnt = queue.popleft()

        if maps[cur_r][cur_c] == "E":
            answer += cnt
            return answer

        for dr, dc in drdc:
            nr, nc = cur_r + dr, cur_c + dc

            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and maps[nr][nc] != "X":
                    visited[nr][nc] = True
                    queue.append((nr, nc, cnt + 1))

    return -1