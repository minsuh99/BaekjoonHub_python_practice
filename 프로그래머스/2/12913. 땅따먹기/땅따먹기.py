def solution(land):
    my_list = [[0 for _ in range(4)] for _ in range(len(land))]
    my_list[-1] = land[-1]
    
    for i in range(len(my_list) - 2, -1, -1):
        for j in range(len(my_list[i])):
            my_list[i][j] = land[i][j] + max([my_list[i+1][k] for k in range(len(my_list[i+1])) if k != j])
    return max(my_list[0])