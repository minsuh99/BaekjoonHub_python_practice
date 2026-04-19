def solution(s):
    cnt_p = 0
    cnt_y = 0
    for c in s:
        if c in ["p", "P"]:
            cnt_p += 1
        elif c in ["y", "Y"]:
            cnt_y += 1
            
    return True if cnt_p == cnt_y else False