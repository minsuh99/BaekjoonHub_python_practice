def solution(n, arr1, arr2):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    answer = []
    for i in range(n):
        num1 = arr1[i]
        num2 = arr2[i]
        
        bin1 = bin(num1)[2:]
        bin2 = bin(num2)[2:]
        
        for j in range(len(bin1)):
            arr[i][n - j - 1] = int(bin1[-(j + 1)])
        
        for k in range(len(bin2)):
            arr[i][n - k - 1] += int(bin2[-(k + 1)])
    
    for i in range(n):
        temp = ''
        for j in arr[i]:
            if j > 0:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    
    return answer