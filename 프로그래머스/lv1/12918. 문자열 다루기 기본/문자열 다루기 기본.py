def solution(s):
    answer = True if s.isdigit() and len(s) in [4, 6] else False
    return answer