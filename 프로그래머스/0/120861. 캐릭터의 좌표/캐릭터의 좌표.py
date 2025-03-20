def solution(keyinput, board):
    max_width = board[0] // 2
    max_height = board[1] // 2
    
    cur = [0, 0]
    
    for key in keyinput:
        if key == "left":
            cur[0] = max((-1) * max_width, cur[0] - 1)
        elif key == "right":
            cur[0] = min(max_width, cur[0] + 1)
        elif key == "down":
            cur[1] = max((-1) * max_height, cur[1] - 1)
        elif key == "up":
            cur[1] = min(max_height, cur[1] + 1)
    return cur