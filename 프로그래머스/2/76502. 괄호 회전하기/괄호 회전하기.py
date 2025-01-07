def check_vaild_str(s: str):
    stack = []
    mapping_table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for char in s:
        if char not in mapping_table:
            stack.append(char)
        elif not stack or mapping_table[char] != stack.pop():
            return False
    return len(stack) == 0



def solution(s):
    answer = 0
    for x in range(len(s)):
        check_s = [s[(i + x) % len(s)] for i in range(len(s))]
        answer += check_vaild_str(check_s)
    return answer