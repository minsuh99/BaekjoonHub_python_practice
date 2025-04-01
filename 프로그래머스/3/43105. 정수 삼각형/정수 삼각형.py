def solution(triangle):
    # 위 -> 아래 방향은 중간중간 경우의 수가 많음
    # 아래 -> 위 방향으로 계산,, (어쨌든 결과는 맨 아래 숫자를 만나야 끝나니까)
    # 바로 위로 올라갈때, 왼쪽과 오른쪽 중 더 큰 숫자를 위로 올라가면서 더하면 됨.
    # 참고함
    
    my_list = [[0] * i for i in range(1, len(triangle)+1)]
    my_list[-1] = triangle[-1]
    
    for i in range(len(my_list) - 2, -1, -1):
        for j in range(len(triangle[i])):
            my_list[i][j] += triangle[i][j] + max(my_list[i+1][j], my_list[i+1][j+1])
    
    return my_list[0][0]
    