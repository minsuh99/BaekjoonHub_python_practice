from collections import deque
S = int(input())

# (screen, clipboard, cnt)
queue = deque([(1, 0, 0)])
visited = [[False for _ in range(S + 1)] for _ in range(S + 1)]
visited[1][0] = True

while queue:
    screen, clipboard, cnt = queue.popleft()

    if screen == S:
        print(cnt)
        exit()
    
    # 1) copy
    if not visited[screen][screen]:
        visited[screen][screen] = True
        queue.append((screen, screen, cnt + 1))

    # 2) paste
    if clipboard > 0 and screen + clipboard <= S:
        if not visited[screen + clipboard][clipboard]:
            visited[screen + clipboard][clipboard] = True
            queue.append((screen + clipboard, clipboard, cnt + 1))

    # 3) delete
    if screen > 0:
        if not visited[screen - 1][clipboard]:
            visited[screen - 1][clipboard] = True
            queue.append((screen - 1, clipboard, cnt + 1))