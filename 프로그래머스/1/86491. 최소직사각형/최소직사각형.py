def solution(sizes):
    answer = 0
    width, height = 0, 0
    
    for size in sizes:
        width = max(width, max(size[0], size[1]))
        height = max(height, min(size[0], size[1]))
    
    answer = width * height
    return answer