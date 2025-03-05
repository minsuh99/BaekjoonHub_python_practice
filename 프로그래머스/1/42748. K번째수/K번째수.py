def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = map(int, command)
        check_array = sorted(array[i-1:j])
        answer.append(check_array[k-1])
        
    return answer