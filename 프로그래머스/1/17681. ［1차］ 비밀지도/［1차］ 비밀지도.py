def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        target1 = arr1[i]
        target2 = arr2[i]
        cur_row = ''
        for j in range(n):
            if target1 % 2 == 0 and target2 % 2 == 0:
                cur_row += " "
            else:
                cur_row += "#"
            target1 //= 2
            target2 //= 2
        answer.append(cur_row[::-1])
    return answer