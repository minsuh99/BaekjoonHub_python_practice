def solution(sizes):
    answer = 0
    max_w, max_h = 0, 0
    for size in sizes:
        size[0], size[1] = max(size[0], size[1]), min(size[0], size[1])
        max_w, max_h = max(max_w, size[0]), max(max_h, size[1])
    
    answer = max_w * max_h
    return answer