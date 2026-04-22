def solution(s):
    my_list = [int(i) for i in s.split()]
    answer = f"{min(my_list)} {max(my_list)}"
    return answer