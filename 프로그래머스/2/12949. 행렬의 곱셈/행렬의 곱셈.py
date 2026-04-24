def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    for r in range(len(arr1)):
        for c in range(len(arr2[0])):
            answer[r][c] = sum([arr1[r][i] * arr2[i][c] for i in range(len(arr1[0]))])
    
    return answer