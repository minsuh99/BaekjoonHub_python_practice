from collections import deque


def solution(players, m, k):
    answer = 0
    cur_server = 0
    queue = deque([]) # (증설 시간, 증설한 서버 수)
    for t in range(24):
        if queue and queue[0][0] + k == t:
            _, server = queue.popleft()
            cur_server -= server
        
        if players[t] > 0:
            need_server = players[t] // m - cur_server
            if need_server > 0:
                cur_server += need_server
                queue.append((t, need_server))
                answer += need_server

    return answer