def solution(dirs):
    answer = set()
    dir_dict = dict({"U":(0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0)})
    cur_x, cur_y = 0, 0
    
    for d in dirs:
        dx, dy = dir_dict[d]
        if -5 <= cur_x + dx <= 5 and -5 <= cur_y + dy <= 5:
            answer.add((cur_x, cur_y, cur_x + dx, cur_y + dy))
            answer.add((cur_x + dx, cur_y + dy, cur_x, cur_y))
            cur_x += dx
            cur_y += dy

    return len(answer) // 2