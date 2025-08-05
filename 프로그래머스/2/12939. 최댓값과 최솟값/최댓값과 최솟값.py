def solution(s):
    answer = ''
    my_list = list(map(int, s.split()))
    answer = str(min(my_list)) + ' ' + str(max(my_list))
    return answer