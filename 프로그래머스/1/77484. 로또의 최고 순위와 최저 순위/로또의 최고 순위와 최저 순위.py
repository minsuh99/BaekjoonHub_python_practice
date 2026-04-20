def solution(lottos, win_nums):
    answer = []
    cnt_zero = lottos.count(0)
    correct_num = 0
    my_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for lotto in lottos:
        if lotto == 0:
            continue
        if lotto in win_nums:
            correct_num += 1
    answer.append(my_dict[correct_num + cnt_zero])
    answer.append(my_dict[correct_num])
    
    return answer